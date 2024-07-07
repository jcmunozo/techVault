#django
from django.shortcuts import redirect, render, get_object_or_404
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

