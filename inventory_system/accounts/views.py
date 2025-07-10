from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
    
class CusotmLoginView(LoginView):
    template_name = 'accounts/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')