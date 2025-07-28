from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from .forms import CustomSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created successfully. You can now log in.")
        return response
    
class CusotmLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return reverse_lazy("admin-dashboard")
        return reverse_lazy('dashboard')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You are successfully logged in.")
        return response
    
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, "You have been logged out.")
        return super().dispatch(request, *args, **kwargs)
    
    