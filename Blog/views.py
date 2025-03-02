from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.utils import timezone
from .models import Post, Category, Tag


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

def recommended(request):
    recommended = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at').first()
    return render(request, 'blog/recommended.html', {'recommended': recommended})

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_details.html', {'post': post})

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'blog/category_list.html', context)

def tag_list(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'blog/tags_list.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)

def PrivacyPolicy(request):
    context = {}
    return render(request, 'blog/privacy-policy.html', context)

def TermsConditions(request):
    context = {}
    return render(request, 'blog/terms-conditions.html', context)

def disclaimer(request):
    context = {}
    return render(request, 'blog/disclaimer.html', context)