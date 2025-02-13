from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

# def index(request):
#    return render(request, 'blog/index.html')

def BlogPost(request):
    posts = Post.object.all()
    return render(request, 'blog/index.html', {"posts": post})