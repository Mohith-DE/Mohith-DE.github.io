from django.shortcuts import render, redirect            # Import render and redirect functions
from django.contrib import messages                   # Import messages framework for displaying messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm        # Import forms for user registration and profile updates
from django.contrib.auth import logout                  # Import logout function to log out users
from django.contrib.auth.decorators import login_required    # Import login_required decorator to protect views


# Create your views here.
def register(request): 
    if request.method == 'POST': 
        form = UserRegisterForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account is created! You can now log in {username}.')
            return redirect('login')
  
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout_view(request): 
    logout(request)
    return render(request, 'users/logout.html')

@login_required # Decorator to ensure the user is logged in to access this view
def profile(request): 
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST, instance=request.user)  
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form, 
            'p_form': p_form
        }

    return render(request, 'users/profile.html', context)


