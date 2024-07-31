"""Features Urls"""
#django
from django.urls import path

#features
from . import views

app_name = 'features'

urlpatterns = [
    path("features/",views.features, name="list"),
    path("create_feature/<int:tech_id>",views.create_feature, name="create"),
    path("delete_feature/<slug:slug>",views.DeleteFeature.as_view(), name="delete"),
    path("feauture/<slug:slug>",views.DetailFeature.as_view(), name="detail"),
    path("update_feature/<slug:slug>",views.UpdateFeature.as_view(), name="update"),
]
