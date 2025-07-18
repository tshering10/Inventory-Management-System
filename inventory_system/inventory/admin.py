from django.contrib import admin
from inventory.models import Category, Product, ContactMessage, Supplier
# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','category','quantity','price', 'brand','created_at', 'updated_at']
    
admin.site.register(Product, ProductAdmin)


@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", 'email', 'message', 'created_at']
    
@admin.register(Supplier)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["company_name", 'email', 'phone', 'address', 'created_at']
    
