from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.db.models import Count
from .models import Post, Category, Author
from .forms import CommentForm

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 8
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_post'] = Post.objects.filter(is_featured=True).first()
        context['recommended_posts'] = Post.objects.order_by('-published_date')[:5]
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/article.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_posts'] = Post.objects.exclude(id=self.object.id).order_by('?')[:5]
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('post_detail', slug=self.object.slug)
        
        context = self.get_context_data(object=self.object)
        context['comment_form'] = form
        return self.render_to_response(context)

class CategoryView(ListView):
    model = Post
    template_name = 'blog/travel.html'
    context_object_name = 'posts'
    paginate_by = 8
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(categories=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['recommended_posts'] = Post.objects.order_by('-published_date')[:5]
        return context

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'blog/about.html'
    context_object_name = 'author'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object)[:5]
        context['recommended_posts'] = Post.objects.order_by('-published_date')[:5]
        return context