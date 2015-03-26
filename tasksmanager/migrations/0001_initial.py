# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('description', models.CharField(max_length=1000, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('client_name', models.CharField(max_length=1000, verbose_name='\u5ba2\u6237\u7684\u540d\u5b57\u662f\uff1f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.CharField(max_length=1000, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('time_elapsed', models.IntegerField(default=None, null=True, verbose_name='\u4efb\u52a1\u6240\u6d88\u8017\u65f6\u95f4', blank=True)),
                ('importance', models.IntegerField(verbose_name='\u4efb\u52a1\u91cd\u8981\u6027')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d\u5b57')),
                ('login', models.CharField(max_length=25, verbose_name='\u767b\u5f55')),
                ('password', models.CharField(max_length=100, verbose_name='\u5bc6\u7801')),
                ('password_bis', models.CharField(max_length=100, verbose_name='\u786e\u8ba4\u8f93\u5165\u7684\u5bc6\u7801')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('born_date', models.DateField(default=None, null=True, verbose_name='\u51fa\u751f\u65e5\u671f', blank=True)),
                ('last_connection', models.DateTimeField(default=None, null=True, verbose_name='\u6700\u540e\u8fde\u63a5\u65e5\u671f', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='\u7535\u5b50\u90ae\u7bb1\u5730\u5740')),
                ('years_seniority', models.IntegerField(default=0, verbose_name='\u8d44\u5386\u5982\u4f55')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='\u4f55\u65f6\u8fc7\u751f\u65e5\uff1f', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasksmanager.UserProfile')),
                ('specialisation', models.CharField(max_length=50, verbose_name='\u7279\u522b\u6307\u6d3e\u7684\u7ba1\u7406\u8d26\u6237')),
            ],
            options={
            },
            bases=('tasksmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='tasksmanager.UserProfile')),
                ('supervisor', models.ForeignKey(verbose_name='\u6b64\u5f00\u53d1\u8005\u7684\u7ba1\u7406\u8005\u662f\uff1f', to='tasksmanager.Supervisor')),
            ],
            options={
            },
            bases=('tasksmanager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(verbose_name='\u4efb\u52a1\u6240\u5c5e\u5f00\u53d1\u8005', to='tasksmanager.Developer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, blank=True, to='tasksmanager.Project', null=True, verbose_name='\u6240\u5c5e\u54ea\u4e2a\u9879\u76ee'),
            preserve_default=True,
        ),
    ]
