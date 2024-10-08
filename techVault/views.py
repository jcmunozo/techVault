"""Admin Views"""
# Django
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

# Tech
from techs.models import Tech

# Creator
from creators.models import Creator

class Home(ListView):
    model = Tech
    template_name = 'app/home.html'
    context_object_name = 'objects'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("search")
        
        if self.request.user.is_authenticated:
            tech_queryset = Tech.objects.filter(user=self.request.user)
        else:
            queryset = Tech.objects.filter(visibility=True)
        
        if search_query:
            tech_queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            ).distinct()

            creator_queryset = Creator.objects.filter(
                Q(name__icontains=search_query) |
                Q(biography__icontains=search_query)
            ).distinct()

            combined_queryset = list(tech_queryset) + list(creator_queryset)
            return combined_queryset

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query']=self.request.GET.get("search","")
        return context

def about(request):
    return render(request, 'app/about.html')
