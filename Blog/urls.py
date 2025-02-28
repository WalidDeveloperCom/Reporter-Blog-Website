from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('latest/', views.latest_post, name='latest_post'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
]
