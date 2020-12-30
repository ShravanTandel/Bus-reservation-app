from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30, unique = True)
    registereddate = models.DateField()

    def __str__(self):
        return self.name


class BusInfo(models.Model):
    busno = models.CharField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departuretime = models.TimeField(max_length = 10)
    date = models.DateField()
    bustype = models.CharField(max_length = 10, choices = (("AC","AC"),("NON AC","NON AC")))
    duration = models.CharField(max_length = 10)
    price = models.IntegerField()
    rate = models.FloatField(null = True, default = 5.0)

    def __str__(self):
        return self.busno

class Seats(models.Model):
    seatno = models.CharField(max_length=30)
    busno = models.ForeignKey(BusInfo, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.seatno


class Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='passenger', null = True)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length = 10, choices = (("M","M"),("F","F")))
    date = models.DateField()
    age = models.IntegerField()
    emailid = models.EmailField()
    phoneno = models.CharField(max_length = 20)
    busno = models.ForeignKey(BusInfo, on_delete=models.CASCADE)
    seatno = models.ForeignKey(Seats, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Rating(models.Model):
    rate = models.IntegerField(choices = ((1,1),(2,2),(3,3),(4,4),(5,5)), default = 5)
    passenger = models.ForeignKey(Passenger, on_delete = models.CASCADE)
    bus = models.ForeignKey(BusInfo, on_delete = models.CASCADE)
    experience = models.TextField(null = True)