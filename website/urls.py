from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_views
urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', blog_views.index),
    url(r'^register/$', blog_views.register),
    url(r'^login/$', blog_views.login),
    url(r'^logout/$', blog_views.logout),
    url(r'^add-post/$', blog_views.add_post),
    url(r'^(?P<username>(\w+))/$', blog_views.user_posts),
    url(r'^(?P<username>(\w+))/post(?P<post_id>[0-9]+)/$', blog_views.post),
]
