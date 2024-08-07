from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('', views.Home.as_view(), name='home'),
    path('', include('techs.urls')),
    path('', include('users.urls')),
    path('', include('features.urls')),
    path('', include('creators.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path("select2/", include("django_select2.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
