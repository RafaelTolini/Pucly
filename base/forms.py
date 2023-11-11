from django.forms import ModelForm
from .models import ForumPost, Answer, Profile


class ForumCreation(ModelForm):
  class Meta:
    model = ForumPost
    fields = ('title','tags', 'text',)

class AnswerCreation(ModelForm):
  class Meta:
    model = Answer
    fields = ('text',)

class ProfilePictureUpdate(ModelForm):
  class Meta:
    model = Profile
    fields = ('profile_picture',)
