from django.shortcuts import render
from Profile.models import Profile
# Create your views here.
def profile_view(request):
    profile = request.user.profile
    return render(request, "profile/profile_view.html", {"profile":profile})