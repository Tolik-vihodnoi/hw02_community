from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Group, Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pub_date')[:10]
    context: dict[str:str] = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context: dict[str:str] = {
        'title': 'Записи сообщества %s' % slug,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
