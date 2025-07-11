from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from .forms import CustomSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    
class CusotmLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return reverse_lazy("admin-dashboard")
        return reverse_lazy('user-dashboard')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
class UserDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user_dashboard.html'
    login_url = reverse_lazy('login')

class AdminDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/admin_dashboard.html'
    