from django.shortcuts import redirect, render
from django.shortcuts import redirect, render, get_object_or_404
from .forms import Create_new_feature
from .models import Feature
from techs.models import Tech
from django.contrib.auth.decorators import login_required


@login_required
def features(request):
    features = Feature.objects.filter(user=request.user)
    return render(request, 'features/list.html', {
        'features':features
    })

@login_required
def create_feature(request, tech_id):
    tech = get_object_or_404(Tech, id=tech_id)
    if request.method == 'GET':
        return render(request, 'features/create.html',{
            'form': Create_new_feature(),
            'tech':tech
        })
    else:
        form = Create_new_feature(request.POST, request.FILES)
        if form.is_valid():
            new_feature = form.save(commit=False)
            new_feature.tech = tech
            new_feature.user = request.user
            new_feature.save()
        return redirect('features:list')

