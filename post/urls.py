"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
# from django.contrib import admin
from . import views
from django.conf.urls import url



urlpatterns = [

    url(r'^(?P<pk>\d+)/post/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/pt/$', views.read_more, name='read_more'),
    url('post/new/', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/post/edit/$', views.post_edit, name='post_edit'),
    #url(r'^(?P<pk>\d+)/post/favourite/$', views.favourite_post, name='favourite_post'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^like/', views.like_post, name='like_post'),
    url(r'^favourite/', views.favourite_post, name='favourite_post'),
    url(r'^comment/', views.post_edit, name='post_edit'),
    url(r'filter/', views.filter, name='filter'),
    url(r'other/', views.other, name='other'),
    url(r'editForm/', views.editForm, name='editForm'),
    url(r'favourites/', views.favourite_post_list, name='favourite_post_list'),
    url(r'likes/', views.like_post_list, name='like_post_list'),
    url(r'^(?P<pk>\d+)/remove/post/$', views.post_remove, name='post_remove'),
    #url(r'^(?P<pk>\d+)/remove/image/$', views.image_remove, name='image_remove'),
    #url(r'^(?P<pk>\d+)/comment/post/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^(?P<pk>\d+)/comment/remove/$', views.comment_remove, name='comment_remove'),
    #url(r'^(?P<pk>\d+)/comment/edit/$', views.comment_edit, name='comment_edit'),
    url(r'', views.home, name='home'),
]   
