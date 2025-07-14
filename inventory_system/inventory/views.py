from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from inventory.models import Product
from inventory.forms import Product_Create_Form

# Create your views here.

class HomeView(TemplateView):
    template_name = "inventory/home.html"

class AdminDashboard(TemplateView):
    template_name = "inventory/admin_dashboard.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "inventory/user_dashboard.html"
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(owner = self.request.user)

class ProductCreateView(CreateView):
    form_class = Product_Create_Form
    template_name = "inventory/add_product.html"
    success_url = reverse_lazy("dashboard")
    
class EditProductView(LoginRequiredMixin,UpdateView):
    model = Product
    template_name = "inventory/edit_product.html"
    fields = ['name','quantity','price','brand','category','owner']
    success_url = reverse_lazy('dashboard')
    
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "inventory/delete_product.html"
    success_url = reverse_lazy("dashboard")
    
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner