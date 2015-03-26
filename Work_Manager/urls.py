from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'tasksmanager.views.index',
                           name='public_index'),
                       url(r'^create-developer$',
                           'tasksmanager.views.create_developer', name='create_developer'),
                       url(r'^create-project/$',
                           'tasksmanager.views.create_project', name='create_project'),
                       url(r'^tm', include('tasksmanager.urls')),
                       url(r'^create-supervisor$',
                           'tasksmanager.views.create_supervisor', name='create_supervisor'),
                       url(r'^create-task$',
                           'tasksmanager.views.create_task', name='create_task'),
                       url(r'^project_list$',
                           'tasksmanager.views.project_list', name='project_list'),
                       url(r'^project-detail(?P<pk>\d+)$', 'tasksmanager.views.project_detail', name='project_detail'),
                       url(r'^task_list$', 'tasksmanager.views.task_list',
                           name='task_list'),
                       url(r'^task_detail_(?P<pk>\d+)$',
                           'tasksmanager.views.task_detail', name='task_detail'),
                       url(r'^task-search-ajax/$',
                           'tasksmanager.views.task_ajax', name='task_search_ajax'),
                       )