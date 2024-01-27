from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserSignupForm, UserSigninForm


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password1)
            user.is_active = True
            form = user.save()

            if form is not None:
                print('user created successfully')
            else:
                print('user not created')

            return redirect('login')
    else:
        form = UserSignupForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserSigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('news_page')
            else:
                messages.error(request, 'Username or password is incorrect')
                return redirect('login')
    else:
        form = UserSigninForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('dashboard')
