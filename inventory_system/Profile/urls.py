from django.urls import path
from Profile.views import profile_view, profile_edit_view

urlpatterns = [
    path("",profile_view, name="profile-view"),
    path("edit-profile",profile_edit_view, name="edit-profile"),
]
