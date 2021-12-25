from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("registration/", views.registerPage, name="registerPage"),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logoutUser"),
]

