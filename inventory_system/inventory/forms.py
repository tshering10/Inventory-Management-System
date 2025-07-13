from django import forms
from inventory.models import Product

class Product_Create_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','quantity','price','brand','category','owner']