from django.shortcuts import render
from techs.models import Tech
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    queryset = request.GET.get("search")
    techs = Tech.objects.all()
    if queryset:
        techs = Tech.objects.filter(
            Q(name__icontains = queryset) |
                Q(description__icontains = queryset)
        ).distinct()

    paginator = Paginator(techs, 2)
    page = request.GET.get('page')
    techs = paginator.get_page(page)

    return render(request, 'home.html', {
        'techs':techs,
    })

def about(request):
    return render(request, 'about.html')
