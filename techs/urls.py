"""Techs Urls"""
#django
from django.urls import path

#techs
from . import views

app_name = 'techs'

urlpatterns = [
    path("techs/",views.techs, name="list"),
    path("create_tech/",views.create_tech, name="create"),
    path("techs/<slug:slug>",views.tech_detail, name="detail"),
    path("update/<slug:slug>",views.UpdateTech.as_view(), name="update"),
]
