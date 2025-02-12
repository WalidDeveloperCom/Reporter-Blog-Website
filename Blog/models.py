from django.db import models
from django.contrib.auth.models import User

# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# Tag model
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Author model - Assuming you're associating with the Django User model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png')
    bio = models.TextField(max_length=200, default='No bio...')
    email = models.EmailField(max_length=100, blank=False, unique=True, default=False)
    password = models.CharField(max_length=100, blank=False, default=False)

    def __str__(self):
        return self.user.username

# Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
