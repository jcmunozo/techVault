"""Creators Urls"""
# Django
from django.urls import path

# Creators
from .views import *

app_name = 'creators'

urlpatterns = [
    path("list_creators/",ListCreators.as_view(), name="list"),
    path("create_creator/",CreateCreator.as_view(), name="create"),
    path("detail_creator/<slug:slug>",DetailCreator.as_view(), name="detail"),
    path("update_creator/<slug:slug>",UpdateCreator.as_view(), name="update"),
    path("delete_creator/<slug:slug>",DeleteCreator.as_view(), name="delete"),
]
