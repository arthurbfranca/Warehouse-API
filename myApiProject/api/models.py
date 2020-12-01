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
    role = models.CharField(max_length=100, default="Worker")

    def __str__(self):
        return '%s %s' % (self.name, self.role)



class Warehouse(models.Model):
    Warehouse_id = models.IntegerField(primary_key=True, default= 0)
    address = models.CharField(max_length= 100)
    admin_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.Warehouse_id, self.admin_id, self.address)


class Item(models.Model):
    Item_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length= 100)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Dimensions = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self):
        return self.Name

    
class Vehicule(models.Model):
    Vehicule_id = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=10)
    model = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s %s' % (self.model, self.size)
    
    
class Works_At(models.Model):
    Worker_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (('Worker_id', 'Warehouse_id'))
        
    def __str__(self):
        return '%s %s' % (self.Worker_id,  self.Warehouse_id)
    
    
#class Transaction(models.Model):
#   WH_Receiver_id = models.ForeignKey(Warehouse, on_delete= )