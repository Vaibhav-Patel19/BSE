from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
from main.models import barOrder, foodOrder
from .models import Payment

def PaymentGateway(request):

    totalAmount = 0
    foodItem = foodOrder.objects.all().filter(user = request.user)
    barItem = barOrder.objects.all().filter(user = request.user)


    user = request.user
    email = request.user.email

    if request.method == 'POST':

        client = razorpay.Client(auth=("rzp_test_ktKHbW267TNArC", "OBcqpAYQbFtXjP7TJ2QQfvNT"))

        DATA = {
            "amount": totalAmount,
            "currency": "INR",
        }
        payment = client.order.create(data = DATA)

    for item in foodItem:
        totalAmount += item.price * item.quantity

    for item in barItem:
        totalAmount += item.price * item.quantity

    if(Payment.objects.all().filter(user = request.user).count() == 1):
        pay = Payment.objects.update(user=request.user, total = totalAmount, bill_paid = False)
    else:
        pay = Payment.objects.create(user = request.user, total = totalAmount, bill_paid = False)

    display_amount = totalAmount
    totalAmount = totalAmount * 100

    return render(request, "payment.html", {'display_amount' : display_amount, 'totalAmount': totalAmount, 'user': user, 'email': email })


@csrf_exempt
def success(request):

    p = Payment.objects.all().filter(user = request.user).update(bill_paid = True)
    p.save()

    return render(request, "success.html")
