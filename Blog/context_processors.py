from .models import Category, Post

def categories_processor(request):
    categories = Category.objects.annotate(post_count=Count('posts')).order_by('name')
    recent_posts = Post.objects.order_by('-published_date')[:5]
    
    return {
        'categories': categories,
        'recent_posts': recent_posts,
    }

