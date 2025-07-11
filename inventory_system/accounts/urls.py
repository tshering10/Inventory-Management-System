from django.urls import path
from accounts.views import SignupView, CusotmLoginView, CustomLogoutView, UserDashboard, AdminDashboard
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CusotmLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('dashboard/', UserDashboard.as_view(), name='user-dashboard'),
    path('admin-dashboard/', AdminDashboard.as_view(), name='admin-dashboard'),
]
