from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Group, Post, User


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
    posts = group.posts.select_related('author', 'group')
    page_number = request.GET.get('page')
    paginator = Paginator(posts, settings.NUM_OF_POSTS)
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    page_number = request.GET.get('page')
    posts_owner = get_object_or_404(User, username=username)
    posts = posts_owner.posts.select_related('author', 'group')
    paginator = Paginator(posts, settings.NUM_OF_POSTS)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'posts_owner': posts_owner
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post_pk = request.GET.get('post_id')
    print(post_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)
