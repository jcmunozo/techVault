from django.urls import path
from . import views

app_name = 'techs'

urlpatterns = [
    path("", views.home, name="home"),
    path("techs/",views.techs, name="list"),
    path("logout/",views.signout, name="logout"),
    path("login/",views.signin, name="login"),
    path("signup/",views.signup, name="signup"),
    path("create_tech/",views.create_tech, name="create"),
    path("techs/<slug:slug>",views.tech_detail, name="detail"),
]
