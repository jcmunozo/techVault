"""Features Urls"""
#django
from django.urls import path

#features
from . import views

app_name = 'features'

urlpatterns = [
    path("features/",views.features, name="list"),
    path("create_feature/<int:tech_id>",views.create_feature, name="create"),
]
