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

#Works at
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
