from django.template import Library
from django.template.defaultfilters import timesince_filter
from django.utils import translation

register = Library()

@register.filter
def timesince_pt(value, arg=None):
    with translation.override('pt'):
        time_since = timesince_filter(value, arg)
    return time_since