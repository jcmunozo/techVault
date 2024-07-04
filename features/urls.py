from django.urls import path
from . import views

urlpatterns = [
    path("feature/",views.feature, name="feature"),
    path("create_feature/",views.create_feature, name="create_feature"),
]
