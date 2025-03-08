from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.utils import timezone
from .models import Post, Category, Tag

def index(request):
    categories = Category.objects.annotate(post_count=Count('post'))
    tags = Tag.objects.annotate(post_count=Count('post'))
    latest_post = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')[:1]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')

    try:
        if page_number is None or int(page_number) < 1:
            page_number = 1
    except (TypeError, ValueError):
        page_number = 1

    print(f"Page number: {page_number}") 

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'latest_post': latest_post,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/index.html', context)

def latest_post(request):
    latest_post = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at').first()
    return render(request, 'blog/latest_post.html', {'latest_post': latest_post})

def recommended(request):
    recommended = Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at').first()
    return render(request, 'blog/recommended.html', {'recommended': recommended})

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_details.html', {'post': post})

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def travel(request):
    context = {}
    return render(request, 'blog/travel.html', context)

def lifestyle(request):
    context = {}
    return render(request, 'blog/lifestyle.html', context)

def cruises(request):
    context = {}
    return render(request, 'blog/cruises.html', context)

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
