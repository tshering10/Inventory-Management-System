from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'password1', 'password2']