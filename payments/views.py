from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
from main.models import barOrder, foodOrder

def PaymentGateway(request):

    totalAmount = 0
    foodItem = foodOrder.objects.all().filter(user = request.user)
    barItem = barOrder.objects.all().filter(user = request.user)

    for item in foodItem:
        totalAmount += item.price * item.quantity

    for item in barItem:
        totalAmount += item.price * item.quantity

    user = request.user
    email = request.user.email


    if request.method == 'POST':

        client = razorpay.Client(auth=("rzp_test_ktKHbW267TNArC", "OBcqpAYQbFtXjP7TJ2QQfvNT"))

        DATA = {
            "amount": totalAmount,
            "currency": "INR",
        }
        payment = client.order.create(data = DATA)
    
    display = totalAmount
    totalAmount = totalAmount * 100

    return render(request, "payment.html", {'display' : display, 'totalAmount': totalAmount, 'user': user, 'email': email })


@csrf_exempt
def success(request):
    return render(request, "success.html")
