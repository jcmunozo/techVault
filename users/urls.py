from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("logout/",views.signout, name="logout"),
    path("login/",views.signin, name="login"),
    path("signup/",views.signup, name="signup"),
]
