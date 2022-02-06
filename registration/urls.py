from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("registration/", views.registerPage, name="registerPage"),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logoutUser"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

