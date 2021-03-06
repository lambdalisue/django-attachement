from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^registration/login/$', 'django.contrib.auth.views.login',
        name='login'),
    url(r'^registration/logout/$', 'django.contrib.auth.views.logout',
        name='logout'),
    url(r'^', include('miniblog.blogs.urls')),
    url(r'^attachment/', include('attachment.urls')),

)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
)
