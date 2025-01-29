from .forms import ForumCreation
from .models import Tag

def navbar_context(request):
    form = ForumCreation()
    tags = Tag.objects.all()
    context_data = {
        'nav_form':form,
        'nav_tags':tags,
    }
    return context_data