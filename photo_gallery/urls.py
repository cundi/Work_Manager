from django.conf.urls import url, patterns
from .views import photo

urlpatterns = patterns('',
                       url(r'_gallery(?P<pk>\d+)', photo, name='photos'),
                       )