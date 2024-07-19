"""Techs Views"""
#django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

#techs
from .forms import Create_new_tech
from .models import Tech

#features
from features.models import Feature

@method_decorator(login_required, name="dispatch")
class UpdateTech(UpdateView):
    model = Tech
    template_name = 'techs/update.html'
    form_class = Create_new_tech
    success_url = reverse_lazy('techs:list')

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
        form = Create_new_tech(request.POST, request.FILES)
        if form.is_valid():
            new_feature = form.save(commit=False)
            new_feature.user = request.user
            new_feature.save()
        return redirect('techs:list')


@login_required
def tech_detail(request, slug):
    tech = get_object_or_404(Tech, slug=slug)
    features = Feature.objects.filter(tech_id = tech.id)
    return render(request, 'techs/detail.html',{
        'tech':tech,
        'features':features
    })
