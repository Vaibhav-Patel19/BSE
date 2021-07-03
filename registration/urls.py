from django.urls import path
from . import views

urlpatterns = [
    path("", views.registerPage, name="registerPage"),
    path("login/", views.loginPage, name="loginPage"),
]

