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
        user = self.request.user

        # Authenticated users see their own techs/creators; anonymous visitors
        # only see techs explicitly marked public (visibility=True).
        if user.is_authenticated:
            tech_queryset = Tech.objects.filter(user=user)
            creator_queryset = Creator.objects.filter(user=user)
        else:
            tech_queryset = Tech.objects.filter(visibility=True)
            creator_queryset = Creator.objects.none()

        search_query = self.request.GET.get("search")
        if search_query:
            techs = tech_queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            ).distinct()

            creators = creator_queryset.filter(
                Q(name__icontains=search_query) |
                Q(biography__icontains=search_query)
            ).distinct()

            return list(techs) + list(creators)

        return tech_queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query']=self.request.GET.get("search","")
        return context

def about(request):
    return render(request, 'app/about.html')
