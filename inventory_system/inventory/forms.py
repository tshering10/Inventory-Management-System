from django import forms
from inventory.models import Product, ContactMessage, Category, Supplier
import re

class ProductForm(forms.ModelForm):
    category = forms.CharField(
        max_length=100,
        label="Category Name"
    )
    class Meta:
        model = Product
        fields = ['name','quantity','price','brand','category']
     
    def clean_category(self):
        category_name = self.cleaned_data['category'].strip()
        if not category_name:
            raise forms.ValidationError("Category name cannot be empty.")
        
        category, created = Category.objects.get_or_create(name=category_name)
        return category   
    
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['company_name', 'email', 'phone', 'address']
        
        def clean_phone(self):
            phone = self.cleaned_data.get("phone")
            if not re.match(r'^\+?\d{7,15}$', phone):
                raise forms.ValidationError("Enter a valid phone number.")
            return phone