from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    store_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['store_name', 'username', 'email', 'password1', 'password2']     
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
            
        if commit:
            user.save()
            user.profile.store_name = self.cleaned_data['store_name'] #saving  store name to user's profile 
            user.profile.save()
        return user