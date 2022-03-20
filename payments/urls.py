from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("payments/", views.PaymentGateway, name="paymentsGateway"),
    path("payments/success", views.success, name="success"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)