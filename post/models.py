# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, auth


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, blank = True, related_name = 'likes')
    favourite = models.ManyToManyField(User, blank = True, related_name = 'favourite')
   

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title 


    def total_likes(self):
        return self.likes.count()   

    
   
class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    text = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return '{}'.format(str(self.post.title)) 


class Images(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to = 'static/images/', blank=True, null='True')



    def __str__(self):
        return self.post.title+ "Image" 


class Profile(models.Model):
    #post = models.ForeignKey(Post, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to = 'static/profile/', blank=True, null='True', default="/static/default/defaul.png")



    def __str__(self):
        return "Profile of user {}".format(self.user.username) 
