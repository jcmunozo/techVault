#django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

#models
from .forms import Create_new_tech
from .models import Tech
from features.models import Feature

def home(request):
    techs = Tech.objects.all()
    return render(request, 'home.html', {
        'techs':techs
    })

@login_required
def techs(request):
    techs = Tech.objects.filter(user=request.user)
    return render(request, 'techs/list.html', {
        'techs':techs
    })

@login_required
def create_tech(request):
    if request.method == 'GET':
        return render(request, 'techs/create.html',{
            'form': Create_new_tech()
        })
    else:
        Tech.objects.create(name=request.POST['name'],slug=request.POST['slug'], user=request.user)
        return redirect('techs:home')

@login_required
def tech_detail(request, slug):
    tech = get_object_or_404(Tech, slug=slug)
    features = Feature.objects.filter(tech_id = tech.id)
    return render(request, 'techs/detail.html',{
        'tech':tech,
        'features':features
    })

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
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
                return redirect('techs:home')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password do not match'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('techs:home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
            )
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('techs:home')
