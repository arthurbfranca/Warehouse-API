from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

class UserList (APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer (users, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail (APIView):

    def get(self, request, pk, format=None):
        user = User.objects.get (pk=pk)
        serializer = UserSerializer(user)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=request.data)
        print(user)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = User.objects.filter (pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View all Customer/Add a new one
class CustomerList (APIView):
    def get(self, request, format=None):
        c = Customer.objects.all()
        serializer = CustomerSerializer (c, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CustomerDetail (APIView):

    def get(self, request, pk, format=None):
        c = Customer.objects.get (pk=pk)
        serializer = CustomerSerializer(c)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        c = Customer.objects.filter(pk=pk).first()
        serializer = CustomerSerializer(c, data=request.data)
        print(c)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        c = Customer.objects.filter (pk=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View all Drivers
class DriverList (APIView):
    def get(self, request, format=None):
	    driver = Employee.objects.filter(role='driver')
	    serializer = EmployeeSerializer (driver, many=True)
	    return Response(serializer.data)

# View individual drivers
class DriverDetail (APIView):

    def get(self, request, pk, format=None):
        emp = Employee.objects.get (pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        emp = Employee.objects.filter(pk=pk).first()
        serializer = EmployeeSerializer(emp, data=request.data)
        print(emp)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Employee.objects.filter (pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View all Employees/Add a new one
class EmployeeList (APIView):
    def get(self, request, format=None):
        emps = Employee.objects.all()
        serializer = EmployeeSerializer (emps, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View a specific employee
class EmployeeDetail (APIView):

    def get(self, request, pk, format=None):
        emp = Employee.objects.get (pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        emp = Employee.objects.filter(pk=pk).first()
        serializer = EmployeeSerializer(emp, data=request.data)
        print(emp)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emp = Employee.objects.filter (pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View all Warehouses
class WarehouseList (APIView):
    def get(self, request, format=None):
        whs = Warehouse.objects.all()
        serializer = WarehouseSerializer (whs, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = WarehouseSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View a specific Warehouse
class WarehouseDetail (APIView):
	def get(self, request, pk, format=None):
		whs = Warehouse.objects.filter(pk=pk)
		serializer = WarehouseSerializer(whs, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		whs = Warehouse.objects.filter(pk=pk).first()
		serializer = WarehouseSerializer(whs, data=request.data)
		print(whs)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		whs = Warehouse.objects.filter (pk=pk)
		whs.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# View all Items
class ItemList (APIView):
    def get(self, request, format=None):
        items = Item.objects.all()
        serializer = ItemSerializer (items, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = ItemSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View specific items
class ItemDetail (APIView):
	def get(self, request, pk, format=None):
		item = Item.objects.filter(pk=pk)
		serializer = ItemSerializer(item, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		item = Item.objects.filter(pk=pk).first()
		serializer = ItemSerializer(item, data=request.data)
		print(item)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		item = Item.objects.filter (pk=pk)
		item.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# View all Routes
class RouteList (APIView):
    def get(self, request, format=None):
        routes = Route.objects.all()
        serializer = RouteSerializer (routes, many=True)
        return Response(serializer.data);

    def post(self, request, format=None):
        serializer = RouteSerializer (data=request.data)
        if serializer.is_valid( ):
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View a specific route
class RouteDetail (APIView):
	def get(self, request, pk, format=None):
		route = Route.objects.filter(pk=pk)
		serializer = RouteSerializer(route, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		route = Route.objects.filter(pk=pk).first()
		serializer = RouteSerializer(route, data=request.data)
		print(route)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		route = Route.objects.filter (pk=pk)
		route.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
# View Works at
class WorksList (APIView):
    def get(self, request, format=None):
	    worksat = Works_At.objects.all()
	    serializer = RouteSerializer (worksat, many=True)
	    return Response(serializer.data)

    def post(self, request, format=None):
	    serializer = WorksSerializer (data=request.data)
	    if serializer.is_valid ():
	    	serializer.save ()
	    	return Response (serializer.data, status=status.HTTP_201_CREATED)
	    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ShipList (APIView):
    def get(self, request, format=None):
	    s = Ship.objects.all()
	    serializer = ShipSerializer (s, many=True)
	    return Response(serializer.data)

    def post(self, request, format=None):
	    serializer = ShipSerializer (data=request.data)
	    if serializer.is_valid ():
	    	serializer.save ()
	    	return Response (serializer.data, status=status.HTTP_201_CREATED)
	    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
