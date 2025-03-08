from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('travel/', views.travel, name='travel'),
    path('lifestyle/', views.lifestyle, name='lifestyle'),
    path('cruises/', views.cruises, name='cruises'),
    path('contact/', views.contact, name='contact'),
    path('latest/', views.latest_post, name='latest_post'),
    #path('category_list/', views.category_list, name='category_list'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('privacy-policy/', views.PrivacyPolicy, name='privacy-policy'),
    path('terms-conditions/', views.TermsConditions, name='terms-conditions'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
]
