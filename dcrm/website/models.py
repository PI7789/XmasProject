from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class Custom_User(AbstractUser):
    phonenum = models.CharField(max_length=14, blank=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True, editable = False)
    booking_user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_adults = models.IntegerField(default=0)
    booking_children = models.IntegerField(default=0)
    booking_oap = models.IntegerField(default=0)
    booking_total_cost = models.FloatField(default=0)

class Payment(models.Model):
    card_num = models.CharField(max_length=16, blank=True)
    Expiry_Date = models.CharField(max_length=5, blank=True)
    Card_Name = models.CharField(max_length=40, blank=True)
    security_code = models.CharField(max_length=3, blank=True)