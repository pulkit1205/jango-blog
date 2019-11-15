# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Images
from .models import Profile




class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'dob', 'photo')




admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Profile, ProfileAdmin)
