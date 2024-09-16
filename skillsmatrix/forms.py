from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email is now required
    username = forms.CharField(required=False)  # Username is optional

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Ensure email is saved

        # If username is not provided, use email as username
        if not self.cleaned_data['username']:
            user.username = user.email

        if commit:
            user.save()
        return user
