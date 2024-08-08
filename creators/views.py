"""Creators Views"""
# Django
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Creators
from .forms import Create_new_creator
from .models import Creator

@method_decorator(login_required, name="dispatch")
class ListCreators(ListView):
    model = Creator
    paginate_by = 3
    template_name='creators/list.html'
    context_object_name='creators'

@method_decorator(login_required, name="dispatch")
class CreateCreator(CreateView):
    model = Creator
    form_class = Create_new_creator
    template_name = 'creators/create.html'
    success_url = reverse_lazy('creators:list')

    def form_valid(self, form):
        """Add user to context"""
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class DetailCreator(DetailView):
    model = Creator
    template_name = 'creators/detail.html'
    context_object_name='creator'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

@method_decorator(login_required, name="dispatch")
class UpdateCreator(UpdateView):
    model = Creator
    template_name = 'creators/update.html'
    form_class = Create_new_creator
    success_url = reverse_lazy('creators:list')

@method_decorator(login_required, name="dispatch")
class DeleteCreator(DeleteView):
    model = Creator
    success_url=reverse_lazy("creators:list")
    context_object_name='creator'
    template_name = 'creators/delete.html'
