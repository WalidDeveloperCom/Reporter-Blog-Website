from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

# Author model - Assuming you're associating with the Django User model
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png')
    bio = models.TextField(max_length=200, default='No bio...')

    def __str__(self):
        return self.user.username

# Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
