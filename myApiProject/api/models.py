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
    Id = models.IntegerField(primary_key= True, serialize= True, default= 0)
    name = models.CharField(max_length= 50)
    address = models.CharField(max_length= 100)
    role = models.CharField(max_length=100, default="Worker")

    def __str__(self):
        return '%s %s' % (self.name, self.role)



class Warehouse(models.Model):
    Warehouse_id = models.IntegerField(primary_key=True, default= 0, serialize= True)
    address = models.CharField(max_length= 100)
    admin_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.Warehouse_id, self.admin_id, self.address)


class Item(models.Model):
    Item_id = models.IntegerField(primary_key=True, serialize=True, default= 0)
    Name = models.CharField(max_length= 100)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Dimensions = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.Name


class Vehicle(models.Model):
    Vehicle_id = models.IntegerField(primary_key=True, serialize= True)
    size = models.CharField(max_length=10)
    model = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.model, self.size)


class Works_At(models.Model):
    Worker_id = models.ForeignKey(Employee, on_delete=models.CASCADE, serialize=True)
    Warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, serialize=True)

    class Meta:
        unique_together = (('Worker_id', 'Warehouse_id'))

    def __str__(self):
        return '%s %s' % (self.Worker_id,  self.Warehouse_id)


class Route(models.Model):
    Route_id = models.IntegerField(primary_key=True,serialize= True)
<<<<<<< HEAD
    Path = models.CharField(max_length= 200)

class Transaction(models.Model):
   Transaction_id = models.IntegerField(primary_key= True, serialize= True)
   WH_Receiver_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Sender_id')
   WH_Sender_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Receiver_id')
   Driver_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, blank = True)
   Route_id = models.ForeignKey(Route, null=True, on_delete=models.SET_NULL, blank = True)
=======
    Path = models.CharField(max_length= 200)    
    
    def __str__(self):
        return '%s %s' % (self.Route_id,  self.Path)
    
class Transaction(models.Model):
    Transaction_id = models.IntegerField(primary_key= True, serialize= True)
    WH_Receiver_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Sender_id')
    WH_Sender_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Receiver_id')
    Driver_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, blank = True)
    Route_id = models.ForeignKey(Route, null=True, on_delete=models.SET_NULL, blank = True)
   
    def __str__(self):
        return '%s %s %s' % (self.Transaction_id,  self.WH_Receiver_id, self.WH_Sender_id)
   
class Customer(models.Model):
    Cid = models.IntegerField(primary_key= True, serialize= True)
    Caddress = models.CharField(max_length= 100)
    Name = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s %s %s' % (self.Cid,  self.Caddress, self.Name)

class Ship(models.Model):
    Driver_id = models.ForeignKey(Employee, null= True, default= None, blank= True, on_delete=models.SET_NULL)
    Item_id = models.ForeignKey(Item, on_delete=models.CASCADE ,serialize= True)
    Cid = models.ForeignKey(Customer, on_delete=models.CASCADE, serialize= True)
    Route_id = models.ForeignKey(Route, null= True, default= None, blank = True, on_delete =models.SET_NULL)
    Quantity = models.IntegerField(default=1)
    Status = models.BooleanField(default= False)    ##false is incomplete
    
    def __str__(self):
        return '%s %s %s %r' % (self.Item_id,  self.Cid, self.Quantity, self.Status)

    class Meta:
        unique_together = (('Cid', 'Item_id'))

class Subsection(models.Model):
    Warehouse_id = models.ForeignKey(Warehouse, on_delete= models.CASCADE, serialize= True)
    Name = models.CharField(max_length= 100, serialize= True)
    Total_space = models.DecimalField(decimal_places= 2, max_digits= 8, default= 100)
    
    def __str__(self):
        return '%s %s %r' % (self.Warehouse_id,  self.Name, self.Total_space)
    
    class Meta:
        unique_together = (('Warehouse_id', 'Name'))

    
class Store(models.Model):
    Warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE, serialize=True)
    Subsection_name = models.ForeignKey(Subsection, on_delete=models.CASCADE,serialize= True )
    Item_id = models.ForeignKey(Item, on_delete= models.CASCADE, serialize=True)
    Quantity = models.IntegerField(default= 1)
    
    def __str__(self):
        return '%s %s %r %r' % (self.Warehouse_id,  self.Subsection_name, self.Item_id, self.Quantity)
    
    class Meta:
        unique_together = (('Warehouse_id', 'Subsection_name','Item_id'))
        
class Transfer(models.Model):
    Item_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    WH_Receiver_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Sender_id')
    WH_Sender_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Receiver_id', null = True)
    Transaction_id = models.ForeignKey(Transaction, serialize= True, on_delete=models.CASCADE, primary_key= True)
    
    def __str__(self):
        return '%s %s %s' % (self.Transaction_id,  self.WH_Receiver_id, self.WH_Sender_id)
    
class Request(models.Model):
    Admin_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    WH_Receiver_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Sender_id')
    WH_Sender_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Receiver_id', null= True)
    Transaction_id = models.ForeignKey(Transaction, serialize= True, on_delete=models.CASCADE, primary_key= True)
    
    def __str__(self):
        return '%s %s %s %s' % (self.Admin_id,  self.WH_Receiver_id, self.WH_Sender_id, self.Transaction_id)
    

class Issue(models.Model):
    Exec_id = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    WH_Receiver_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Sender_id')
    WH_Sender_id = models.ForeignKey(Warehouse, on_delete = models.DO_NOTHING, related_name= 'WH_Receiver_id')
    Transaction_id = models.ForeignKey(Transaction, serialize= True, on_delete=models.CASCADE, primary_key= True)
    
    def __str__(self):
        return '%s %s %s %s' % (self.Exec_id,  self.WH_Receiver_id, self.WH_Sender_id, self.Transaction_id)
    
class Drive(models.Model):
    Vehicle_id = models.ForeignKey(Vehicle, on_delete = models.CASCADE, serialize= True)
    Driver_id = models.ForeignKey(Employee, on_delete = models.CASCADE, serialize= True)
    
    def __str__(self):
        return '%s %s' % (self.Vehicle_id,  self.Driver_id)
    
    class Meta:
        unique_together = (('Vehicule_id', 'Driver_id'))
   
 
>>>>>>> 417b1af878bab7741b7c2502289aa472fa2fd22a
