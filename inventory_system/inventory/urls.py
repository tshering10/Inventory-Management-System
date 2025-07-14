from django import urls
from django.urls import path
from inventory.views import HomeView, ProductListView, AdminDashboard, ProductCreateView, EditProductView, ProductDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', ProductListView.as_view(), name='dashboard'),
    path('admin-dashboard', AdminDashboard.as_view(), name='admin-dashboard'),
    path('add-product', ProductCreateView.as_view(), name="add-product"),
    path('product/<int:pk>/edit/', EditProductView.as_view(), name="edit-product"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="delete-product"),
]
