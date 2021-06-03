from django.contrib import admin

from .models import Comment, Notification, Post, ThreadModel, UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(ThreadModel)