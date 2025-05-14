from django.contrib import admin
from .models import ContactSubmission
from .models import StaticPage


@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject')
