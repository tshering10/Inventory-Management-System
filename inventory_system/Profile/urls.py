from django.urls import path
from Profile.views import profile_view

urlpatterns = [
    path("",profile_view, name="profile-view"),
]
