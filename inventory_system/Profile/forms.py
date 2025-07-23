from django import forms
from Profile.models import Profile
from django.contrib.auth.models import User

        

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','bio', 'address', 'phone']
        
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']