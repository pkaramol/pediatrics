"""the_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import (HomeView, AboutView, BlogListView, BlogPostCreateView,
                    ContactView, BlogPostDetailView)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='site-home'),
    url(r'^about/$', AboutView.as_view(), name='site-about'),
    url(r'^contact/$', ContactView.as_view(), name='site-contact'),
    url(r'^blog/$', BlogListView.as_view(), name='blog'),
    url(r'^blogpost-create/$', BlogPostCreateView.as_view(),
        name='blogpost-create'),
    url(r'^blogpost/(?P<pk>\d+)/$', BlogPostDetailView.as_view(),
        name='blogpost-detail'),

    # url(r'^blogposts/', BlogHomeListView.as_view(), name='blogpost-list'),
    # url(r'^create/$', BlogPostCreateView.as_view(), name="blogpost-create"),
    # url(r'^update/(?P<pk>\d+)/$', BlogPostUpdateView.as_view(), name="blogpost-update"),
    # url(r'^delete/(?P<pk>\d+)/$', BlogPostDeleteView.as_view(), name="blogpost-delete"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
