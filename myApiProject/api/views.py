from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.db.models import Sum

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
        
#View the information of a given customer, edit his info, and delete him from db.
class CustomerDetail (APIView):

    def get(self, request, pk, format=None):
        c = Customer.objects.get (pk=pk)
        serializer = CustomerSerializer(c)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        c = Customer.objects.filter(pk=pk).first()
        serializer = CustomerSerializer(c, data=request.data)
        print(c)
        if serializer.is_valid ( ) and c.Cid == request.data["Cid"]:
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        c = Customer.objects.filter (pk=pk)
        c.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# View all "Drive," linking a driver to a shipment
class DriveList (APIView):
    def get(self, request, format=None):
        c = Drive.objects.all()
        serializer = DriveSerializer (c, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = DriveSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View all Drivers
class DriverList (APIView):
    def get(self, request, format=None):
	    driver = Employee.objects.filter(role='driver')
	    serializer = EmployeeSerializer (driver, many=True)
	    return Response(serializer.data)

# View individual drivers (DO WE NEED THIS)????????
class DriverDetail (APIView):

    def get(self, request, pk, format=None):
        emp = Employee.objects.get (Id=pk)
        serializer = EmployeeSerializer(emp)
        return Response (serializer.data)

    #undone atm
    def delete(self, request, pk, format=None):
        emp = Employee.objects.filter (pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
		
# View all Workers
class WorkerList (APIView):
    def get(self, request, format=None):
	    worker = Employee.objects.filter(role='worker')
	    serializer = EmployeeSerializer (worker, many=True)
	    return Response(serializer.data)

# View all Admins
class AdminList (APIView):
    def get(self, request, format=None):
	    admin = Employee.objects.filter(role='admin')
	    serializer = EmployeeSerializer (admin, many=True)
	    return Response(serializer.data)
	
# View all executives	
class ExecutiveList (APIView):
    def get(self, request, format=None):
	    executive = Employee.objects.filter(role='exec')
	    serializer = EmployeeSerializer (executive, many=True)
	    return Response(serializer.data)
		
# View a given driver's vehicle
class DriverVehicle (APIView):

    def get(self, request, pk, format=None):
        drive = Drive.objects.get(Driver_id=pk)
        serializer1 = DriveSerializer(drive)
        key = serializer1.data["Vehicle_id"]
        v = Vehicle.objects.get (Vehicle_id=key)
        serializer2 = VehicleSerializer(v)
        return Response (serializer2.data)

# View a given driver's shipments
class DriverShipments (APIView):

    def get(self, request, pk, format=None):
        s = Ship.objects.get(Driver_id=pk)
        serializer = ShipSerializer(s)
        return Response (serializer.data)
        
# View specific shipment of a driver
class DriverShipmentDetail (APIView):

    def get(self, request, pk, item, cid, route, format=None):
        s = Ship.objects.get (Driver_id=pk,Item_id=item,Cid=cid,Route_id=route)
        serializer = ShipSerializer(s)
        return Response (serializer.data)
        
    def put(self, request, pk, item, cid, route, format=None):
        s = Ship.objects.get (Driver_id=pk,Item_id=item,Cid=cid,Route_id=route)
        if(request.data == "True" or request.data == "true" or request.data == True):
            s.Status = True
        if(request.data == "False" or request.data == "false"):
            s.Status = False  
        serializer = ShipSerializer(s)
        return Response (serializer.data)

# View a given driver's transactions
class DriverTransactions (APIView):

    def get(self, request, pk, format=None):
        s = Transaction.objects.get(Driver_id=pk)
        serializer = TransactionSerializer(s)
        return Response (serializer.data)

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

class SubsectionList (APIView):
    def get(self, request, format=None):
        subsection = Subsection.objects.all()
        serializer = SubsectionSerializer (subsection, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = SubsectionSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubsectionDetail (APIView):
	def get(self, request, pk, format=None):
		subsection = Subsection.objects.filter(pk=pk)
		serializer = SubsectionSerializer(subsection, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		subsection = Subsection.objects.filter(pk=pk).first()
		serializer = SubsectionSerializer(subsection, data=request.data)
		print(subsection)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		subsection = Subsection.objects.filter (pk=pk)
		subsection.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
		
# View specific items
class StoreDetail (APIView):
	def get(self, request, pk, format=None):
		store = Store.objects.filter(pk=pk)
		serializer = StoreSerializer(store, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		store = Store.objects.filter(pk=pk).first()
		serializer = ItemSerializer(store, data=request.data)
		print(store)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		store = Store.objects.filter (pk=pk)
		store.delete()
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

# View Stores
class StoreList (APIView):
    def get(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer (store, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View specific items
class StoreDetail (APIView):
	def get(self, request, pk, format=None):
		store = Store.objects.filter(pk=pk)
		serializer = StoreSerializer(store, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		store = Store.objects.filter(pk=pk).first()
		serializer = ItemSerializer(store, data=request.data)
		print(store)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		store = Store.objects.filter (pk=pk)
		store.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		
# View all Routes/add a new one
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
	    serializer = WorksSerializer (worksat, many=True)
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
        
# View a specific route
class ShipDetail (APIView):
	def get(self, request, pk, format=None):
		route = Ship.objects.filter(pk=pk)
		serializer = ShipSerializer(route, many=True)
		return Response(serializer.data)
		
	def put(self, request, pk, format=None):
		route = Ship.objects.filter(pk=pk).first()
		serializer = ShipSerializer(route, data=request.data)
		print(route)
		if serializer.is_valid ( ):
			print(request.data)
			serializer.save()
			return Response (serializer.data)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request, pk, format=None):
		route = Ship.objects.filter (pk=pk)
		route.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionList (APIView):
    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer (transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer (data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TransactionDetail (APIView):
    def get(self, request, pk, format=None):
        transaction = Transaction.objects.filter(pk=pk)
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
		
    def put(self, request, pk, format=None):
        transaction = Transaction.objects.filter(pk=pk).first()
        serializer = TransactionSerializer(transaction, data=request.data)
        print(transaction)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
    def delete(self, request, pk, format=None):
        transaction = Transaction.objects.filter (pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RequestList (APIView):
    def get(self, request, format=None):
        request = Request.objects.all()
        serializer = RequestSerializer (request, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RequestDetail (APIView):
    def get(self, request, pk, format=None):
        request = Request.objects.filter(pk=pk)
        serializer = RequestSerializer(request, many=True)
        return Response(serializer.data)
		
    def put(self, request, pk, format=None):
        request = Request.objects.filter(pk=pk).first()
        serializer = RequestSerializer(request, data=request.data)
        print(request)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
    def delete(self, request, pk, format=None):
        request = Request.objects.filter (pk=pk)
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

class TransferList (APIView):
    def get(self, request, format=None):
        transfer = Transfer.objects.all()
        serializer = TransferSerializer (transfer, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = TransferSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TransferDetail (APIView):
    def get(self, request, pk, format=None):
        transfer = Transfer.objects.filter(pk=pk)
        serializer = TransferSerializer(transfer, many=True)
        return Response(serializer.data)
		
    def put(self, request, pk, format=None):
        id = Transfer.objects.get(Transaction_id = pk)
        transfer = Transfer.objects.filter(pk=id).first()
        serializer = TransferSerializer(transfer, data=request.data)
        print(request)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
    def delete(self, request, pk, format=None):
        transfer = Transfer.objects.filter (pk=pk)
        transfer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class IssueList (APIView):
    def get(self, request, format=None):
        transfer = Issue.objects.all()
        serializer = IssueSerializer (transfer, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = IssueSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IssueDetail (APIView):
    def get(self, request, pk, format=None):
        issue = Issue.objects.filter(pk=pk)
        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)
		
    def put(self, request, pk, format=None):
        issue = Issue.objects.filter(pk=pk).first()
        serializer = IssueSerializer(issue, data=request.data)
        print(request)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
    def delete(self, request, pk, format=None):
        issue = Issue.objects.filter (pk=pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
# View all Routes
class VehicleList (APIView):
    def get(self, request, format=None):
        routes = Vehicle.objects.all()
        serializer = VehicleSerializer (routes, many=True)
        return Response(serializer.data);

    def post(self, request, format=None):
        serializer = VehicleSerializer (data=request.data)
        if serializer.is_valid( ):
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#worker subsections
class WorkerSubsections (APIView):
    def get(self, request, pk, format=None):
        warehouseid = Works_At.objects.filter(Worker_id = pk).first().Warehouse_id
        subsections = Subsection.objects.filter(Warehouse_id = warehouseid)
        serializer = SubsectionSerializer(subsections, many = True)
        return Response(serializer.data)

#subsection worker items
class WorkerItemDetail(APIView):
    def get(self, request, pk, format = None):
        warehouseid = Works_At.objects.filter(Worker_id = pk).first().Warehouse_id
        stores = Store.objects.filter(Warehouse_id = warehouseid).values('Item_id').annotate(Sum('Quantity'))  
        return Response(stores, status=status.HTTP_204_NO_CONTENT)
    
    
    
class WorkerSubsectionDetail (APIView):
    def get(self, request, pk, subid, format= None):
        warehouseid = Works_At.objects.filter(Worker_id = pk).first().Warehouse_id
        stores = Store.objects.filter(Warehouse_id = warehouseid).filter(Subsection_name = subid) 
        serializer = StoreSerializer(stores)
        return Response(serializer.data)
    
    
    def post(self, request, pk, subid, format = None):
        warehouseid = Works_At.objects.filter(Worker_id = pk).first().Warehouse_id
        store = Store.objects.filter(Warehouse_id = warehouseid).filter(Subsection_name = subid)
        serializer = StoreSerializer(store, data=request.data)
        print(store)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)