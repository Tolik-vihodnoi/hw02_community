from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


@login_required
def index(request):
    page_number = request.GET.get('page')
    posts = Post.objects.select_related('author',
                                        'group')
    paginator = Paginator(posts, settings.NUM_OF_POSTS)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author',
                                       'group')
    page_number = request.GET.get('page')
    paginator = Paginator(posts, settings.NUM_OF_POSTS)
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)
