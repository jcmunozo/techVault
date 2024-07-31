"""Features Views"""
#django
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

#techs
from techs.models import Tech

#features
from .forms import Create_new_feature
from .models import Feature


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

class DeleteFeature(DeleteView):
    pass

class DetailFeature(DetailView):
    pass

class UpdateFeature(UpdateView):
    pass
