from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from inventory.models import Product

# Create your views here.

class HomeView(TemplateView):
    template_name = "inventory/home.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "inventory/user_dashboard.html"
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.all()