"""Techs Views"""
#django
from django.forms.widgets import media_property
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
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

@method_decorator(login_required, name="dispatch")
class ListTech(ListView):
    model = Tech
    paginate_by = 3
    template_name='techs/list.html'
    context_object_name='techs'

@method_decorator(login_required, name="dispatch")
class CreateTech(CreateView):
    model = Tech
    form_class = Create_new_tech
    template_name = 'techs/create.html'
    success_url = reverse_lazy('techs:list')

    def form_valid(self, form):
        """Add user to context"""
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name="dispatch")
class DetailTech(DetailView):
    model = Tech
    template_name = 'techs/detail.html'
    context_object_name='tech'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
