from tkinter import CASCADE
from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    idno = models.CharField(max_length=90)
    password = models.CharField(max_length=90)

    def __str__(self):
        return self.fullname

class ContactSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=90)
    sub = models.CharField(max_length=90)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.message


# CHOICES_TYPE = [
#     ("",""),
#     ("Saloon","Saloon"),
#     ("Hatchback","Hatchback"),
#     ("SUV","SUV"),
#     # ("",""),
#     # ("",""),
#     # ("",""),
    

# ]

class Car(models.Model):
    regno = models.CharField(max_length=90)
    type = models.CharField(max_length=90)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # image = models.ImageField()
    manufacturer = models.CharField(max_length=90)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created','-created')

    def __str__(self):
        
        return self.regno


class BookAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    approval = models.BooleanField(default=False)


    def __str__(self):
        return self.user.fullname + ' ' + self.car.type


class TestDrive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.fullname + ' ' + ' - ' + self.car.type


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    buytime = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    is_delivered = models.BooleanField(default=False)