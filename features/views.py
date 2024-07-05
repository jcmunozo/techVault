from django.shortcuts import redirect, render
from .forms import Create_new_feature
from .models import Feature
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def features(request):
    features = Feature.objects.all()
    return render(request, 'features/list.html', {
        'features':features
    })

@login_required
def create_feature(request):
    if request.method == 'GET':
        return render(request, 'features/create.html',{
            'form': Create_new_feature()
        })
    else:
        Feature.objects.create(name=request.POST['name'], description=request.POST['description'], tech_id=1, user=request.user)
        return redirect('features:list')

