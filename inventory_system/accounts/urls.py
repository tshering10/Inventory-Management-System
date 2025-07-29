from django.urls import path
from accounts.views import SignupView, CusotmLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CusotmLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/change_password.html',
        success_url=reverse_lazy('change_password_done')),
        name="change_password"),
    
    path('password-changed/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/change_password_done.html'),
        name="change_password_done"),
    
]
