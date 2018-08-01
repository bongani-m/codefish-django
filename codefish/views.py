from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from .forms import LoginForm, RegistrationForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home.html')

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PasswordResetForm()
        return render(request, 'reset.html', {'form': form})

@login_required()
def protected(request):
    return render(request, 'protected.html')

@login_required()
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('protected')
        else:
            return render(request, 'password_change.html', {'form': form})
    else: 
        form = PasswordChangeForm(request.user)
        return render(request, 'password_change.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('protected')
        else:
            return render(request, 'register.html', {'form': form})
    else: 
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

def logout(request):
    auth_logout(request)
    form  = LoginForm()
    return redirect('home')


def test(request):
    print("yo" )
    
    return ('home')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                auth_login(request, user)
                return redirect('protected')
            else:
                print(form.errors)
                return render(request, 'login.html', {'form': form, 'errors': ['Username and Password combo does not match']})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})