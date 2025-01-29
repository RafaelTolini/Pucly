from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

# Create your models here.

    
# TAG MODEL
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# FORUM MODEL
class ForumPost(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, null=True)
    title = models.CharField(max_length=100, blank=True)
    text = QuillField()
    melhor_resposta = models.BooleanField(default=False)

    anonimo = models.BooleanField(default=False)

    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-created']

    def __str__(self):
        return self.title


# ANSWER MODEL
class Answer(models.Model):
    forum = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = QuillField()

    melhor_resposta = models.BooleanField(default=False)

    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text.plain[0:50]


# USER EXTENSION
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    pontos = models.IntegerField(default=0)

    profile_picture = models.ImageField(null=True, default="profile.png")

    unread_notifications = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# NOTIFICATION MODEL
class Notification(models.Model):
  receiver = models.ForeignKey(User, on_delete=models.CASCADE)
  forum = models.ForeignKey(ForumPost, on_delete=models.CASCADE, null=True)
  sender = models.CharField(max_length=100, null=True)
  text = models.CharField(max_length=200)
  is_read = models.BooleanField(default=False)

  notification_image = models.ImageField(null=True, default="logo.png")

  created = models.DateTimeField(auto_now_add=True)

  class Meta:
        ordering = ['-created']

  def __str__(self):
        return self.text

class ComentarioForum(models.Model):
    forum = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=False)
  
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.text

class ComentarioAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=False)
  
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.text
