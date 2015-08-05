from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', blog_views.index),
    url(r'^post(?P<post_id>[0-9]+)/$', blog_views.post)
]
