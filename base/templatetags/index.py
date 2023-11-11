from django.template import Library

register = Library()


@register.filter
def index(indexable, i):
    if i == ' ':
      return int(indexable[i+1:i+3])
    else:
      return indexable[int(i)]
