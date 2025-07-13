from django import urls
from django.urls import path
from inventory.views import HomeView, ProductListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', ProductListView.as_view(), name='dashboard'),
]
