from django.conf.urls import patterns, url

from .views import UpdateProjectList, task_detail


urlpatterns = patterns('',
                       url(r'update_project/$', UpdateProjectList.as_view(), name='update_project'),
                        url(r'_detail_(?P<pk>\d+)$',task_detail, name='task_detail'),
)