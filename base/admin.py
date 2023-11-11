from django.contrib import admin
from .models import Tag, ForumPost, Answer, Profile, Notification

# Register your models here.

admin.site.register(Tag)
admin.site.register(ForumPost)
admin.site.register(Answer)
admin.site.register(Profile)
admin.site.register(Notification)