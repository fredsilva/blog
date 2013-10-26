from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'Blog.core.views.home', name='home'),
    url(r'^post/(?P<pk>\d+)/$', 'Blog.core.views.post_detail', name='post_detail'),
    # url(r'^Blog/', include('Blog.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
