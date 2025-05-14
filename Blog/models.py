from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def post_count(self):
        return self.posts.count()

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    @property
    def post_count(self):
        return self.posts.count()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='authors/', default='authors/default.jpg')
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=False, default="title-slug")
    content = MarkdownxField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='posts/', default='default_image.jpg')
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts') 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    is_featured = models.BooleanField(default=False)
    read_time = models.PositiveIntegerField(default=3, help_text='Estimated read time in minutes')
    
    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.excerpt and self.content:
            self.excerpt = self.content[:200].replace('&nbsp;', ' ')
        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'