from django.urls import path
from . import views

app_name = 'features'

urlpatterns = [
    path("features/",views.features, name="list"),
    path("create_feature/",views.create_feature, name="create"),
]
