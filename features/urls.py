"""Features Urls"""
#django
from django.urls import path

#features
from .views import *

app_name = 'features'

urlpatterns = [
    path("create_feature/<int:tech_id>",CreateFeature.as_view(), name="create"),
    path("update_feature/<int:pk>",UpdateFeature.as_view(), name="update"),
    path("delete_feature/<int:pk>",DeleteFeature.as_view(), name="delete"),
]
