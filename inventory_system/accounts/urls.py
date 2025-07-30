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
    
    #password reset path links
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html",
        html_email_template_name = "accounts/password_reset_email.html",
        success_url = "/accounts/password-reset-done/"),
        name="password_reset" ),
    
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"),
        name="password_reset_done" ),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/accounts/password-reset-complete/'
    ), name='password_reset_confirm'),

    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
    
        
]
