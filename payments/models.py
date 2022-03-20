from django.db import models
from django.contrib.auth.models import User


class PaymentType(models.Model):

    pTypes = (
        ("1", "Credit Card"),
        ("2", "Debit Card"),
        ("3", "Net Banking"),
        ("4", "UPI"),
    )
    
    mobile_Number = models.IntegerField(default = None)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True)
    payType = models.CharField(choices = pTypes, max_length = 50)
    total = models.IntegerField(null = True)