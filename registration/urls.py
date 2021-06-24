from django.urls import path
from . import views

urlpatterns = [
    path("", views.registerPage, name="registerPage"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="loginPage"),
]

