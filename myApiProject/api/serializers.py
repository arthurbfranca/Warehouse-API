from rest_framework import serializers
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
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