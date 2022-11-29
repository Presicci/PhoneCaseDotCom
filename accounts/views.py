from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if not request.method == 'POST':
        return render(request, 'authenticate/login.html', {})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('There Was An Error Logging In, Try Again...'))
            return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request, ('You logged out of PhoneCase.'))
    return redirect('home')

def register_user(request):
    if not request.method == 'POST':
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!!'))
            return redirect('home')

    return render(request, 'authenticate/register_user.html', {
            'form': form,
        })