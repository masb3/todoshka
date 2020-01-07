from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import SignUpForm, LogInForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('doit:index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('doit:index')


def login(request):
    if request.method == 'POST':
        form = LogInForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('doit:index')
    else:
        form = LogInForm()
    return render(request, 'accounts/login.html', {'form': form})


def changepwd(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            user = form.save()
            #auth_login(request, user)
            update_session_auth_hash(request, user)
            return redirect('doit:index')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'accounts/changepwd.html', {'form': form})