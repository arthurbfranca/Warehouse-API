from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
        
class DriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drive
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = '__all__'

class WorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Works_At
        fields = '__all__'

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ship
        fields = '__all__'
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transaction
        fields = '__all__'
        
class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transfer
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Request
        fields = '__all__'
        
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Issue
        fields = '__all__'
		
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'
		
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = '__all__'
		
class SubsectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subsection
        fields = '__all__'

class ModifyStoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__Quantity__', '__Subsection_id__'