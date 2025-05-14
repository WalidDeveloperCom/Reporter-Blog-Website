from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import StaticPage, ContactSubmission  # Import the models
from .forms import ContactForm  # Import the form

class StaticPageView(DetailView):
    model = StaticPage
    template_name = 'pages/static_page.html'
    context_object_name = 'page'

class PrivacyPolicyView(TemplateView):
    template_name = 'pages/privacy-policy.html'

class TermsConditionsView(TemplateView):
    template_name = 'pages/terms-conditions.html'

class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        # Save form data to the database
        ContactSubmission.objects.create(**form.cleaned_data)

        # Show success message
        messages.success(self.request, 'Your message has been sent successfully!')

        return super().form_valid(form)

def error_404_view(request, exception):
    return render(request, 'pages/404.html', {"exception": exception}, status=404)
