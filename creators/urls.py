
"""Creators Urls"""
#django
from django.urls import path

#creators
from . import views

app_name = 'creators'

urlpatterns = [
    path("creators/",views.creators, name="list"),
    path("create_creator/",views.create_creator, name="create"),
]
