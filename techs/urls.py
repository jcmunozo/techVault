from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tech/",views.tech, name="tech"),
    path("logout/",views.signout, name="logout"),
    path("login/",views.signin, name="login"),
    path("signup/",views.signup, name="signup"),
    path("create_tech/",views.create_tech, name="create_tech"),
    path("tech/<int:id>",views.tech_detail, name="tech_detail"),
]
