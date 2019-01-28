from django.db import models
import random

def generateTrackingCode():
    tracking_code = "LC "

    tracking_code += str(random.randint(10,99))
    tracking_code += " "
    tracking_code += str(random.randint(100,999))
    tracking_code += " "
    tracking_code += str(random.randint(100,999))
    tracking_code += " US"

    return tracking_code

# Create your models here.

class Package(models.Model):
    package_id = models.CharField(max_length=30, primary_key=True, default=generateTrackingCode())
    package_name = models.CharField(max_length=500)
    weight = models.CharField(max_length=30)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    has_arrived = models.BooleanField(default=False)
    customer_name = models.CharField(max_length=500)
    customer_tel = models.CharField(max_length=15)

    def __str__(self):
        return self.package_name
