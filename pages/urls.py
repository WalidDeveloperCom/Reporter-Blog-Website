from django.urls import path
from .views import PrivacyPolicyView, TermsConditionsView, ContactView

urlpatterns = [
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-conditions/', TermsConditionsView.as_view(), name='terms_conditions'),
    path('contact/', ContactView.as_view(), name='contact'),
]