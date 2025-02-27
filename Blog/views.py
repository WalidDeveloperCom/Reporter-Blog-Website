from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.utils import timezone
from .models import Post, Category

def index(request):
    categories = Category.objects.annotate(post_count=Count('post'))
    latest_post = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:1]
    context = {
        'categories': categories,
        'latest_post': latest_post,
    }
    return render(request, 'blog/index.html', context)

def blog_post(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {"posts": posts})

def latest_post(request):
    latest_post = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at').first()
    return render(request, 'blog/latest_post.html', {'latest_post': latest_post})

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_details.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/category_list.html', context)
