from django.conf.urls import patterns, url
from .views import PublisherList, PublisherDetail

urlpatterns = patterns('',
                       url(r'publishers/$', PublisherList.as_view(), name='publisher_list'),
                       url(r'publisher_detail(?P<slug>\d+)/$', PublisherDetail.as_view(), name='publisher_detail'),
                       )