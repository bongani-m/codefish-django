from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'home.html')

@login_required()
def protected(request):
    return render(request, 'protected.html')

def logout(request):
    auth_logout(request)
    form  = LoginForm()
    return redirect('home')

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