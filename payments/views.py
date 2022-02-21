from django.shortcuts import render

# Create your views here.

def PaymentGateway(request):
    return render(request, "payment.html")
