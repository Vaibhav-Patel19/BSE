from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None, null = True)
    bill_paid = models.BooleanField(default = False)
    total = models.IntegerField(null = True)
    

    def __str__(self):
        return str(self.user) + " - " + str(self.bill_paid ) + " | Total = " + str(self.total)

    class Meta:
        verbose_name_plural = "Customer Bill Payments Status"    
        # This class will add a title in DB.
