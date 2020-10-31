from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.http import *
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import SignUpForm


def home(request):
    return render(request, 'frontfiles/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.success(
                request, ('Error Logging In - Please Try Again...'))
            return redirect('login')
    else:
        return render(request, 'frontfiles/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out...'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered...'))
            return redirect('dashboard')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'frontfiles/register.html', context)
