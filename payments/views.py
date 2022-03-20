from django.shortcuts import render


def PaymentGateway(request):
    return render(request, "payment.html")

def success(request):
    return render(request, "success.html")
