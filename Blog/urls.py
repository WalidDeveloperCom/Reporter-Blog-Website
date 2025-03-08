from django.urls import path
from .views import HomeView, PostDetailView, CategoryView, AuthorDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
]