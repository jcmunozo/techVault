
"""Creators Urls"""
#django
from django.urls import path

#creators
from . import views

app_name = 'creators'

urlpatterns = [
    path("creators/",views.creators, name="list"),
    path("create_creator/",views.create_creator, name="create"),
    path("delete_creator/<slug:slug>",views.DeleteCreator.as_view(), name="delete"),
    path("creator/<slug:slug>",views.DetailCreator.as_view(), name="detail"),
    path("update_creator/<slug:slug>",views.UpdateCreator.as_view(), name="update"),
]
