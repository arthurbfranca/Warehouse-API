from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField (max_length=50)
    password = models.CharField(max_length=250)

    class Meta:
        app_label='api'

    def __str__(self):
        return self.username



class Employee(models.Model):
    name = models.CharField(max_length= 50)
    address = models.CharField(max_length= 100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Warehouse(models.Model):
    address = models.CharField(max_length= 100)
    admin_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


