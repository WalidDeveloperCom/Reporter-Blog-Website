from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from . models import Post

# def index(request):
#    return render(request, 'blog/index.html')

def BlogPost(request):
    posts = Post.object.all()
    return render(request, 'blog/index.html', {"posts": post})

def latest_post(request):
    latest_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').first()
    return render(request, 'blog/latest_post.html', {'latest_post': latest_post})
