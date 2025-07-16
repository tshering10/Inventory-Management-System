from django import urls
from django.urls import path
from inventory.views import HomeView, ProductListView, AdminDashboard, ProductCreateView, EditProductView, ProductDeleteView, UserDetails, AboutUs_view, ContactUs_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', ProductListView.as_view(), name='dashboard'),
    path('admin-dashboard', AdminDashboard.as_view(), name='admin-dashboard'),
    path('add-product', ProductCreateView.as_view(), name="add-product"),
    path('product/<int:pk>/edit/', EditProductView.as_view(), name="edit-product"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="delete-product"),
    path('admin-dashboard/<int:pk>/details', UserDetails.as_view(), name="user_details"),
    path("about-us/", AboutUs_view.as_view(), name="about_us"),
    path("contact-us/", ContactUs_view.as_view(), name="contact_us"),
]
