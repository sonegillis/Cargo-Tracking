from django.db import models
import random


def generateTrackingCode():
    tracking_code = "SK"

    tracking_code += str(random.randint(10, 99))
    tracking_code += str(random.randint(100, 999))
    tracking_code += str(random.randint(100, 999))

    print(tracking_code)

    return tracking_code

# Create your models here.


class Package(models.Model):
    package_id = models.CharField(max_length=30, primary_key=True)
    package_name = models.CharField(max_length=500)
    estimated_time_of_departure = models.DateField(null=True)
    estimated_time_of_arrival = models.DateField(null=True)
    senders_name = models.CharField(max_length=300)
    senders_country = models.CharField(max_length=100)
    senders_address = models.CharField(max_length=100)
    receivers_name = models.CharField(max_length=300)
    receivers_country = models.CharField(max_length=100)
    recievers_address = models.CharField(max_length=100)
    item_type = models.CharField(max_length=50)
    weight = models.CharField(max_length=30)
    delivery_fee = models.BigIntegerField(default=3000)

    def __str__(self):
        return self.package_id + " (Receiver: " + self.receivers_name + " ,Sender: " + self.senders_name + ")"

    def save(self):
        if not self.package_id:
            self.package_id = generateTrackingCode()
        super(Package, self).save()


class PackageInfo(models.Model):
    package = models.ForeignKey(Package)
    date = models.DateField()
    time = models.TimeField()
    activity = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    on_hold = models.BooleanField(default=False)
