"""Users Views"""
# Django
from django.shortcuts import redirect, render 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Users
from .forms import SignUpForm

def signup(request):

    if request.method == 'GET':
        return render(request, 'users/signup.html', {
            'form': SignUpForm()
        })

    # Let UserCreationForm handle validation: password match, password
    # strength and unique username are all checked and reported as errors.
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'users/signup.html', {
        'form': form
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

