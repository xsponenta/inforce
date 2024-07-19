from django.db import models
from authentication.models import User
from restaurants.models import Menu

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateField()