from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title