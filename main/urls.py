from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.homePage, name="homePage"),
    path('explore/', views.explorePage, name="explorePage"),
    path('menu/<str:cuisine>', views.showMenu, name="showMenu"),
    path('order/', views.orderPage, name="orderPage"),
]