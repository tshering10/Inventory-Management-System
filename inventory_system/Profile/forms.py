from django import forms
from Profile.models import Profile
from django.contrib.auth.models import User

        

        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['store_name','profile_image','bio', 'address', 'phone']
        
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-cotrol'}),
            'bio': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']