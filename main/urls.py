from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.homePage, name="homePage"),
    path('explore/', views.explorePage, name="explorePage"),
    path('menu/<str:cuisine>', views.showMenu, name="showMenu"),
    path('order/', views.orderPage, name="orderPage"),
    path('barmenu/<str:drinktype>', views.showBarMenu, name="showBarMenu"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)