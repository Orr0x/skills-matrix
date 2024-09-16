from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import ExtendedUser
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

def signup(request, tier):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the `auth_user` table
            # Create an associated ExtendedUser entry
            ExtendedUser.objects.create(
                user=user,
                account_tier=tier,
                is_admin=True  # Automatically make the account creator an admin
            )
            login(request, user)  # Log the user in after signup
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form, 'tier': tier})

# Protect the dashboard view with login required
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')

def select_tier(request):
    return render(request, 'select_tier.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use your email-based form
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Authenticate user based on email and password
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after successful login
            else:
                form.add_error(None, 'Invalid login credentials')

    else:
        form = CustomUserCreationForm()

    return render(request, 'login.html', {'form': form})
