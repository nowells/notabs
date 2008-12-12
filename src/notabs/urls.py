from django.conf.urls.defaults import patterns, url, include, handler500, handler404
from django.contrib import admin
from django.conf import settings
from basic.blog.feeds import BlogPostsFeed

feeds = {
    'blog': BlogPostsFeed,
}

admin.autodiscover()

urlpatterns = patterns('notabs.apps.generic.views',
    url(r'^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^register/$', 'register', name='register'),
    url(r'^blog/', include('basic.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',
    url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

urlpatterns += patterns('',
    url(r'^django-admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^django-admin/(.*)', admin.site.root),
)

# If we are in debug mode (more specifically runserver mode) then make sure to setup static serve handlers for media and django-admin-media
if settings.DEBUG:
    import os
    import django
    django_admin_media_path = os.path.abspath(os.path.join(os.path.dirname(django.__file__), 'contrib', 'admin', 'media'))
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^django-admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': django_admin_media_path}),
    )
