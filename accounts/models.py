# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
import re
import urllib
import hashlib


class profile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=12, blank=True, null=True)
    use_gravatar = models.BooleanField(default=True)
    avatar_url = models.URLField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    favorite = models.ManyToManyField(Topic, verbose_name='fav_user', blank=True, null=True)
    vote = models.ManyToManyField(Topic, verbose_name='vote_user', blank=True, null=True)
    coins = models.IntegerField(default=0, blank=True, null=True)
    location = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return '<userInfo: %s>' % self.user

    def unread_mention(self):
        return self.user.recevied_mentions.filter(read=False)

    def old_mention(self):
        return self.user.recevied_mentions.filter(read=True)[0:5]

    def username(self):
        if self.nickname:
            return self.nickname
        else:
            return self.user.usename

    def latest_activity(self):
        d={}
        d['topic']=self.user.topics.all().filter(deleted=False).order_by('-time_created')[0:10]
        d['post']=self.user.post.all().filter(deleted=False).order_by('-time_created')[0:10]
        return d

    def avatar(self):
        da = ''
        dic ={}
        if self.use_gravatar:
            mail = self.user.email.lower()
            gravatar_url = "http://www.gravater.com/avatar"
            base_url = gravatar_url + hashlib.md5(mail).hexdigest() + "?"
            dic['small'] = base_url + urllib.urlencode({'d': da, 's': '40'})
            dic['middle'] = base_url + urllib.urlencode({'d': da, 's': '48'})
            dic['large'] = base_url + urllib.urlencode({'d': da, 's': '80'})
            return dic
        elif self.avatar_url:
            dic['small'] = self.avatar_url
            dic['middle'] = self.avatar_url
            dic['large'] = self.avatar_url
        return dic

    def get_fav_topic(self):
        return self.favorite.all()

    def get_fav_counts(self):
        return self.favorite.count()

    def get_topic_count(self):
        return self.user.topics.filter(replys=None).count()

    def get_reply_count(self):
        return self.user.topics.exclude(reply=None).count()

    def get_unread_replys(self):
        all_replys = []
        for topic in self.user.topics.filter(is_active=True, replys=None):
            replys = Topic.objects.filter(replys=topic, is_read=False)
            for reply in replys:
                all_replys.append(reply)
            return all_replys
