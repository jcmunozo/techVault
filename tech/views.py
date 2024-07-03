from django.shortcuts import redirect, render, get_object_or_404
from .forms import Create_new_feature, Create_new_tech
from .models import Tech, Feature
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    techs = Tech.objects.all()
    return render(request, 'index.html', {
        'techs':techs
    })

@login_required
def tech(request):
    techs = Tech.objects.filter(user=request.user)
    return render(request, 'techs/tech.html', {
        'techs':techs
    })

@login_required
def feature(request):
    features = Feature.objects.all()
    return render(request, 'features/feature.html', {
        'features':features
    })

@login_required
def create_feature(request):
    if request.method == 'GET':
        return render(request, 'features/create_feature.html',{
            'form': Create_new_feature()
        })
    else:
        Feature.objects.create(name=request.POST['name'], description=request.POST['description'], tech_id=1)
        return redirect('feature')

@login_required
def create_tech(request):
    if request.method == 'GET':
        return render(request, 'techs/create_tech.html',{
            'form': Create_new_tech()
        })
    else:
        Tech.objects.create(name=request.POST['name'], user=request.user)
        return redirect('home')

@login_required
def tech_detail(request, id):
    tech = get_object_or_404(Tech, id=id)
    features = Feature.objects.filter(tech_id = id)
    return render(request, 'techs/tech_detail.html',{
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
                return redirect('home')
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
    return redirect('home')

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
            return redirect('home')

