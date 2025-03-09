from django.urls import path
from .views import HomeView, PostDetailView, CategoryView, TagView, AuthorDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagView.as_view(), name='Tag'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]