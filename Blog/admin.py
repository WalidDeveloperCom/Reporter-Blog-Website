from django.contrib import admin
from .models import Post, Category, Tag, Author, PagesMenu

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields if field.name not in ['Content']]

admin.site.register(PagesMenu)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Author)

# Compare this snippet from blog/admin.py: