from django.shortcuts import render
from django.views.generic import ListView
from techs.models import Tech
from django.db.models import Q

class Home(ListView):
    model = Tech
    template_name = 'home.html'
    context_object_name = 'techs'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            ).distinct()
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query']=self.request.GET.get("search","")
        return context

def about(request):
    return render(request, 'about.html')
