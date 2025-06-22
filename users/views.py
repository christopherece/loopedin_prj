from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile
from posts.models import Post

# The register view is now handled by allauth

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

def user_profile(request, username):
    """View for viewing other users' profiles"""
    profile_user = get_object_or_404(User, username=username)
    
    # Get user's posts
    posts = Post.objects.filter(author=profile_user).order_by('-created_at')[:5]
    
    # Check if this is the current user's profile
    is_own_profile = request.user.is_authenticated and request.user == profile_user
    
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'is_own_profile': is_own_profile
    }
    return render(request, 'users/user_profile.html', context)
