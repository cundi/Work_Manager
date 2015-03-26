from django.conf.urls import patterns, url

from .views import UpdateProjectList


urlpatterns = patterns('',
                       url(r'update_project/$', UpdateProjectList.as_view(), name='update_project')
)