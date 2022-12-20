from django.shortcuts import get_object_or_404, render

from yatube.settings import NUM_OF_POSTS

from .models import Group, Post


def index(request):
    posts = Post.objects.all().select_related('author', 'group')[:NUM_OF_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().select_related('author', 'group')[:NUM_OF_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
