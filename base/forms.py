from django.forms import ModelForm
from .models import ForumPost, Answer, Profile, ComentarioForum, ComentarioAnswer
from django.contrib.auth.models import User


class ForumUpdate(ModelForm):
    class Meta:
        model = ForumPost
        fields = ('text',)

class ForumCreation(ModelForm):
    class Meta:
        model = ForumPost
        fields = (
            'title',
            'tags',
            'text',
        )

class AnswerCreation(ModelForm):
    class Meta:
        model = Answer
        fields = ('text', )


class ProfilePictureUpdate(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture', )


class ComentarioForumForm(ModelForm):
    class Meta:
        model = ComentarioForum
        fields = ('text', )
class ComentarioAnswerForm(ModelForm):
    class Meta:
        model = ComentarioAnswer
        fields = ('text', )


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
        )
