from django.db import models
from django.contrib.auth.models import User
from ..utils.bbs_utils import get_delta_time
import markdown


class ForumThread(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __unicode__(self):
        return self.title


class ForumPost(models.Model):
    thread = models.ForeignKey(ForumThread)
    text = models.TextField()
    pub_date = models.DateTimeField(verbose_name='date published')
    author = models.ForeignKey(User)

    def mdText(self):
        return markdown.markdown(self.text, safe_mode=True)

    def __unicode__(self):
        return "(%s) [%s] %s" % (self.thread, self.author, self.text[0:25])


class Topic(models.Model):
    # the author of current topic
    user = models.ForeignKey(User, verbose_name='topics')
    node = models.ForeignKey('Node', verbose_name='topics')
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    hits = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_read = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)

    def __unicode__(self):
        return '<Topic: %s>' % self.created

    # get user's avatar while showing topics in list
    def get_display_datetime(self):
        return get_delta_time(self.created)

    def get_reply_count(self):
        return Topic.objects.filter(reply=self, is_active=True).count()

    def get_last_reply(self):
        replys = Topic.objects.filter(replys=self, is_active=True).order_by('-time_created')
        if replys:
            return replys[0]
        else:
            return None

    # if user has reading his topic, all topic_set is mark read
    def topic_set_is_read(self, user):
        if self.user == user:
            Topic.objects.filter(replys=self).update(is_read=True)

    class Meta:
        ordering = ['-time_created']


class Node(models.Model):
    pass