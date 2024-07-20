"""Users Views"""
#django
from django.shortcuts import redirect, render 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#users
from .forms import SignUpForm

def signup(request):

    if request.method == 'GET':
        return render(request, 'users/signup.html', {
        'form': SignUpForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                    )
                user.save()
                login(request, user)
                return redirect('home')
            except:
                return render(request, 'users/signup.html', {
                    'form': SignUpForm,
                    'error': 'Username already exist'
                })
        
        return render(request, 'users/signup.html', {
            'form': SignUpForm,
            'error': 'password do not match'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'users/signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
            )
        if user is None:
            return render(request, 'users/signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')

