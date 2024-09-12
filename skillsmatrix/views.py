# skillsmatrix/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def signup(request, tier):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after signup
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form, 'tier': tier})

# Protecting the dashboard view
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')

def select_tier(request):
    return render(request, 'select_tier.html')