from django.urls import path
from accounts.views import SignupView, CusotmLoginView, CustomLogoutView
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CusotmLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
