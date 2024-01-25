from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def user_register(request):
    return render(request, 'accounts/register.html')


def user_login(request):
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('dashboard')
