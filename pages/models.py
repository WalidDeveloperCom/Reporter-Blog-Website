from django.db import models
from markdownx.models import MarkdownxField

class StaticPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = MarkdownxField()
    
    def __str__(self):
        return self.title

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"