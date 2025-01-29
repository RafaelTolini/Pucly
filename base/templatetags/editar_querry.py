from django.template import Library
from ..models import ForumPost
from ..forms import ForumCreation

register = Library()

@register.simple_tag
def editar_querry(pk):
    forum = ForumPost.objects.get(id=pk)
    form = ForumCreation(instance=forum)
    return form