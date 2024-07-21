"""Techs Urls"""
#django
from django.urls import path

#techs
from .views import *

app_name = 'techs'

urlpatterns = [
    path("techs/",ListTech.as_view(), name="list"),
    path("delete_tech/<slug:slug>",DeleteTech.as_view(), name="delete"),
    path("create_tech/",CreateTech.as_view(), name="create"),
    path("tech/<slug:slug>",DetailTech.as_view(), name="detail"),
    path("update_tech/<slug:slug>",UpdateTech.as_view(), name="update"),
]
