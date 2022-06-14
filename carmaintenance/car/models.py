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
