from django.contrib import admin
from inventory.models import Category, Product
# Register your models here.

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','category','quantity','price', 'created_at', 'updated_at']
    
admin.site.register(Product, ProductAdmin)
