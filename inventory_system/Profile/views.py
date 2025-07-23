from django.shortcuts import render, redirect
from Profile.models import Profile
from Profile.forms import ProfileForm, UserForm

# Create your views here.
def profile_view(request):
    profile = request.user.profile
    return render(request, "profile/profile_view.html", {"profile":profile})

def profile_edit_view(request):
    user = request.user
    profile = user.profile
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile-view')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    return render(request, "profile/edit_profile.html", {
        'user_form': user_form,
        'profile_form': profile_form
    })