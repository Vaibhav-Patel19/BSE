from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True)
    bill_paid = models.BooleanField(default = False)
    total = models.IntegerField(null = True)

    bill_status = "Not Paid"
    if(bill_paid == True):
        bill_status = "Paid"
    

    def __str__(self):
        return str(self.user) + " - " + self.bill_status + " | Total = " + str(self.total)

    class Meta:
        verbose_name_plural = "Customer Bill Payments Status"    
        # This class will add a title in DB.
