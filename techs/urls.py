from django.urls import path
from . import views

app_name = 'techs'

urlpatterns = [
    path("techs/",views.techs, name="list"),
    path("create_tech/",views.create_tech, name="create"),
    path("techs/<slug:slug>",views.tech_detail, name="detail"),
]
