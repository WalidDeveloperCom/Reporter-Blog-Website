from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('latest/', views.latest_post, name='latest_post'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
]
