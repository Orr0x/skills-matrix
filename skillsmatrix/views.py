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
            login(request, user, backend='skillsmatrix.backends.EmailBackend')  # Log the user in after signup
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
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user, backend='skillsmatrix.backends.EmailBackend')
            return redirect('dashboard')  # Adjust as needed for your routes
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
