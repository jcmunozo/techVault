"""Features Views"""
# Django
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Techs
from techs.models import Tech

# Features
from .forms import Create_new_feature
from .models import Feature

@method_decorator(login_required, name="dispatch")
class CreateFeature(CreateView):
    model = Feature
    form_class = Create_new_feature
    template_name = 'features/create.html'

    def get_success_url(self):
        tech = self.object.tech
        return reverse_lazy('techs:detail', kwargs={'slug': tech.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech_id'] = self.kwargs.get('tech_id')
        return context

    def form_valid(self, form):
        tech_id = self.get_context_data().get('tech_id')
        if tech_id is not None:
            tech = get_object_or_404(Tech, id=tech_id)
            form.instance.tech = tech
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class UpdateFeature(UpdateView):
    model = Feature
    template_name = 'features/update.html'
    form_class = Create_new_feature

    def get_success_url(self):
        tech = self.object.tech
        return reverse_lazy('techs:detail', kwargs={'slug': tech.slug})

@method_decorator(login_required, name="dispatch")
class DeleteFeature(DeleteView):
    model = Feature
    context_object_name='feature'
    template_name = 'features/delete.html'
    
    def get_success_url(self):
        tech = self.object.tech
        return reverse_lazy('techs:detail', kwargs={'slug': tech.slug})
