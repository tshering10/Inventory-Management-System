from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from inventory.models import Product, Category, Supplier
from inventory.forms import  ContactMessageForm, ProductForm, SupplierForm
from django.contrib.auth.models import User

# Create your views here.

class HomeView(TemplateView):
    template_name = "inventory/home.html"

class AdminDashboard(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model = User
    template_name = "inventory/admin_dashboard.html"
    context_object_name = 'users'
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def get_queryset(self):
        return User.objects.exclude(is_staff=True) # excluding the admin itself the users' list 

class UserDetails(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "inventory/user_details.html"
    context_object_name = "user_profile"
    
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['products'] = Product.objects.filter(owner=self.get_object())   
        return context
    
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    model = Supplier
    template_name = "inventory/user_dashboard.html"
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(owner = self.request.user)
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        user_products = Product.objects.filter(owner=self.request.user)
        
        context['total_products'] = user_products.count()
        # context['total_categories'] = Category.objects.count() #for all the categories in the system
        
        context['total_categories'] = user_products.values('category').distinct().count()
        context['low_stock_count'] = user_products.filter(quantity__lt=10).count()
        
        suppliers = Supplier.objects.filter(owner=self.request.user)
        context['total_suppliers'] = suppliers.values('company_name').distinct().count()

        return context

class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = "inventory/add_product.html"
    success_url = reverse_lazy("dashboard")
    
    def form_valid(self, form):
        product = form.save(commit=False) # Get product object form the form, and yet not saving to database
        # Assigning currently logged in user as a owner
        product.owner = self.request.user
        
        product.save()
        return super().form_valid(form)
    
class EditProductView(LoginRequiredMixin,UpdateView):
    model = Product
    fields = ['name','quantity','price','brand','category','supplier']
    template_name = "inventory/edit_product.html"
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        product = form.save(commit=False)
        product.category = form.cleaned_data['category']
        product.save()
        return super().form_valid(form)
    
    
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "inventory/delete_product.html"
    success_url = reverse_lazy("dashboard")
    
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

class AboutUs_view(TemplateView):
    template_name = "inventory/about_us.html"
    
class ContactUs_view(FormView):
    form_class = ContactMessageForm
    template_name = "inventory/contact_us.html"
    success_url = reverse_lazy("contact_us")
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class SupplierListView(ListView, LoginRequiredMixin):
    model = Supplier
    template_name = "inventory/supplier/supplier_list.html"
    context_object_name = "suppliers"
    
    def get_queryset(self):
        return Supplier.objects.filter(owner=self.request.user)
  
class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "inventory/supplier/supplier_create.html"
    success_url = reverse_lazy('supplier_list')
    
    def form_valid(self, form):
        supplier = form.save(commit=False)
        supplier.owner = self.request.user
        supplier.save()
        return super().form_valid(form)
    
class SupplierUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "inventory/supplier/supplier_update.html"
    success_url = reverse_lazy("supplier_list")
    
    def test_func(self):
        supplier = self.get_object()
        return supplier.owner == self.request.user
    
class SupplierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Supplier
    template_name = "inventory/supplier/supplier_delete.html"
    success_url = reverse_lazy('supplier_list')

    def test_func(self):
        supplier = self.get_object()
        return supplier.owner == self.request.user