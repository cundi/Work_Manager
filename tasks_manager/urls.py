from django.conf.urls import patterns, url

from .views import UpdateProjectList, task_detail, Task_List, task_ajax, project_detail, project_list
from .views import create_task, create_project, create_developer, create_supervisor
from .views import login
urlpatterns = patterns('',
                       url(r'_task$', create_task, name='create_task'),
                       url(r'_project$', create_project, name='create_project'),
                       url(r'_developer$', create_developer, name='create_developer'),
                       url(r'_supervisor$', create_supervisor, name='create_supervisor'),
                       url(r'_project/$', UpdateProjectList.as_view(), name='edit_project'),
                       url(r'ajax/$', task_ajax, name='task_search_ajax'),
                       url(r'task_(?P<pk>\d+)$', task_detail, name='task_detail'),
                       url(r'_project_(?P<pk>\d+)$', project_detail, name='project_detail'),
                       url(r'task$', Task_List.as_view(), name='list_task'),
                       url(r'_project$',project_list, name='project_list'),
                       url(r'_user$', login, name='login'),
                       )