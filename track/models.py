from django.db import models
import random

def generateTrackingCode():
    tracking_code = "LC "

    tracking_code += str(random.randint(10,99))
    tracking_code += " "
    tracking_code += str(random.randint(100,999))
    tracking_code += " "
    tracking_code += str(random.randint(100,999))
    tracking_code += " UK"

    return tracking_code

# Create your models here.

class Package(models.Model):
    package_id = models.CharField(max_length=30, primary_key=True, default=generateTrackingCode())
    package_name = models.CharField(max_length=500)
    estimated_time_of_departure = models.DateField(null=True)
    estimated_time_of_arrival = models.DateField(null=True)
    senders_name = models.CharField(max_length=300)
    senders_country = models.CharField(max_length=100)
    senders_city = models.CharField(max_length=100)
    receivers_name = models.CharField(max_length=300)
    receivers_country = models.CharField(max_length=100)
    recievers_city = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)

    def __str__(self):
        return self.package_name
