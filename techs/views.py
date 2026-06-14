"""Techs Views"""
# Django
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

# Techs
from .forms import Create_new_tech
from .models import Tech

# Features
from features.models import Feature

# Shared mixins
from techVault.mixins import OwnerQuerysetMixin


@method_decorator(login_required, name="dispatch")
class ListTech(OwnerQuerysetMixin, ListView):
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

    def get_queryset(self):
        """Allow viewing techs owned by the user or marked public."""
        return super().get_queryset().filter(
            Q(user=self.request.user) | Q(visibility=True)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tech = self.object
        features = Feature.objects.filter(tech=tech)
        context['features']=features
        return context

@method_decorator(login_required, name="dispatch")
class UpdateTech(OwnerQuerysetMixin, UpdateView):
    model = Tech
    template_name = 'techs/update.html'
    form_class = Create_new_tech
    success_url = reverse_lazy('techs:list')

@method_decorator(login_required, name="dispatch")
class DeleteTech(OwnerQuerysetMixin, DeleteView):
    model = Tech
    success_url=reverse_lazy("techs:list")
    context_object_name='tech'
    template_name = 'techs/delete.html'
