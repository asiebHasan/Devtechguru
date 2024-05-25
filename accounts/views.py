from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect('home')
        else:
            messages.error(request, "incorrect username/password")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "YOUR ARE LOGGED OUT")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registration success")
            return redirect('home')
        else:
            messages.error(request, 'Invalid Data')
            return render(request, 'accounts/registration.html', {'form': form})

    else:
        form = RegisterUserForm()

        return render(request, 'accounts/registration.html', {'form': form})
    