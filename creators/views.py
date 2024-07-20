"""Creators Views"""
#django
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

#creators
from .forms import Create_new_creator
from .models import Creator


@login_required
def creators(request):
    creators = Creator.objects.filter(user=request.user)
    return render(request, 'creators/list.html', {
        'creators':creators
    })

@login_required
def create_creator(request):
    if request.method == 'GET':
        return render(request, 'creators/create.html',{
            'form': Create_new_creator(),
        })
    else:
        form = Create_new_creator(request.POST, request.FILES)
        if form.is_valid():
            new_feature = form.save(commit=False)
            new_feature.user = request.user
            new_feature.save()
        return redirect('creators:list')

