from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,"dashboard.html")

def profile(request):
    return render(request,"profile.html")

def settings(request):
    return render(request,"settings.html")


# Custom form with email field
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if user is already logged in

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after signup
            messages.success(request, 'Your account has been created successfully!')
            return redirect('home')  # Redirect to home after successful signup
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if the user is already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Log in the user
            messages.success(request, 'Successfully logged in.')
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    """Log out the user and redirect to a specified page."""
    auth_logout(request)
    # Redirect to a specific page or render a template.
    # For example, you might want to redirect to the login page:
    return redirect(reverse('login'))