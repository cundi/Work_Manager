# # coding: utf-8
#
# from django.db import models
# from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
#
#
# class WorkUserProfile(models.Model):
#     GENDER_CHOICES = ('男', '女')
#
#     last_name = models.CharField(max_length=50, verbose_name='姓氏')
#     first_name = models.CharField(max_length=50, verbose_name=u'名字')
#     sex = models.BooleanField(choices=GENDER_CHOICES, verbose_name='性别', default=True)
#     login = models.CharField(max_length=25, verbose_name=u'登录名', unique=True)
#     password = models.CharField(max_length=100, verbose_name=u'密码')
#     password_bis = models.CharField(max_length=100, verbose_name=u'确认输入的密码')
#     born_date = models.DateField(verbose_name=u'出生日期', null=True, blank=True, default=None)
#     joined_date = models.DateTimeField(verbose_name='加入日期', auto_created=True, auto_now_add=True)
#     phone = models.CharField(max_length=20, verbose_name=u'电话号码')
#     email = models.EmailField(verbose_name=u'电子邮箱地址', unique=True)
#     years_seniority = models.IntegerField(verbose_name=u'工作年限', default=0)
#     avatar = models.ImageField(verbose_name='用户头像', null=True, blank=True)
#     personal_banner = models.TextField(verbose_name='个性签名', max_length=1000, null=True, blank=True)
#     favourite = models.CharField(verbose_name='兴趣爱好', max_length=300, null=True, blank=True)
#
#     USERNAME_FIELD = ['login', 'email']
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'login', 'password', 'password_bis', 'email']
#
