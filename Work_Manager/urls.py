from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'tasks_manager.views.index', name='public_index'),
                       url(r'^create/', include('tasks_manager.urls', namespace='create')),
                       url(r'^delete', include('tasks_manager.urls', namespace='delete')),
                       url(r'^edit', include('tasks_manager.urls', namespace='edit')),
                       url(r'^search', include('tasks_manager.urls', namespace='search')),
                       url(r'^list-', include('tasks_manager.urls', namespace='list', app_name='tasks_manager')),
                       url(r'^detail', include('tasks_manager.urls', namespace='detail')),
                       url(r'^accounts', include('tasks_manager.urls', namespace='accounts')),
                       url(r'^forum', include('forum.urls', namespace='forums')),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)