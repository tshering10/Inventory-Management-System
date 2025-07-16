from django import forms
from inventory.models import Product, ContactMessage

class Product_Create_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','quantity','price','brand','category','owner']
        
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']