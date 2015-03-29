# coding: utf-8

from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'用户名字')
    login = models.CharField(max_length=25, verbose_name=u'登录')
    password = models.CharField(max_length=100, verbose_name=u'密码')
    password_bis = models.CharField(max_length=100, verbose_name=u'确认输入的密码')
    phone = models.CharField(max_length=20, verbose_name=u'电话号码')
    born_date = models.DateField(
        verbose_name=u'出生日期', null=True, blank=True, default=None)
    last_connection = models.DateTimeField(
        verbose_name=u'最后连接日期', null=True, blank=True, default=None)
    email = models.EmailField(verbose_name=u'电子邮箱地址')
    years_seniority = models.IntegerField(verbose_name=u'资历如何', default=0)
    date_created = models.DateField(null=True,blank=True,verbose_name=u'何时过生日？', auto_now_add=True)

    def __unicode__(self):
        return self.name


class Supervisor(UserProfile):
    specialisation = models.CharField(
        max_length=50, verbose_name=u'特别指派的管理账户',)


class Developer(UserProfile):
    supervisor = models.ForeignKey(Supervisor, verbose_name=u'此开发者的管理者是？')


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'项目名称')
    description = models.CharField(max_length=1000, verbose_name=u'项目描述')
    client_name = models.CharField(max_length=1000, verbose_name=u'客户的名字是？')

    def __unicode__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'任务名称')
    description = models.CharField(max_length=1000, verbose_name=u'任务描述')
    time_elapsed = models.IntegerField(
        verbose_name=u'任务所消耗时间', null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name=u'任务重要性',)
    project = models.ForeignKey(
        Project, verbose_name=u'所属哪个项目', null=True, default=None, blank=True)
    developer = models.ForeignKey(Developer, verbose_name=u'任务所属开发者')

    def __unicode__(self):
        return self.title

    def natural_key(self):
        return (self.title, self.description,
                self.time_elapsed, self.importance, self.project, self.developer)