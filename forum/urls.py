from django.conf.urls import url, patterns
from .views import login, index, newthread

urlpatterns = patterns('',
                       url(r'login/$', login, name='login'),
                       url(r'', index, name='index'),
                       url(r'/newthread/$', newthread, name='newthread'),
                       )