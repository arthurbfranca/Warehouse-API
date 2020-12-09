from django.urls import path,include
from . import views
urlpatterns = [
    path('admins/', views.AdminList.as_view()),
    path('admins/<int:pk>', views.AdminDetail.as_view()),
    path('admins/<int:pk>/workers/', views.AdminWorkers.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>', views.CustomerDetail.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>', views.EmployeeDetail.as_view()),
    path('drivers/', views.DriverList.as_view()),
    path('drive/', views.DriveList.as_view()),
    path('drivers/<int:pk>', views.DriverDetail.as_view()),
    path('drivers/<int:pk>/vehicle/', views.DriverVehicle.as_view()),
    path('drivers/<int:pk>/shipments/', views.DriverShipments.as_view()),
    path('drivers/<int:pk>/shipments/<int:item>/<int:cid>/<int:route>', views.DriverShipmentDetail.as_view()),
    path('drivers/<int:pk>/transactions/', views.DriverTransactions.as_view()),
	path('routes/', views.RouteList.as_view()),
	path('routes/<int:pk>', views.RouteDetail.as_view()),
	path('warehouses/', views.WarehouseList.as_view()),
	path('warehouses/<int:pk>', views.WarehouseDetail.as_view()),
    path('warehouses/<int:pk>/items/', views.WarehouseInventoryList.as_view()),
	path('subsections/', views.SubsectionList.as_view()),
	path('subsections/<int:pk>', views.SubsectionDetail.as_view()),
    path('items/', views.ItemList.as_view()),
    path('itemstotal/', views.ItemTotalList.as_view()),
	path('items/<int:pk>', views.ItemDetail.as_view()),
	path('stores/', views.StoreList.as_view()),
	path('stores/<int:pk>', views.StoreDetail.as_view()),
    path('worksat/', views.WorksList.as_view()),
    path('shipments/', views.ShipList.as_view()),
    path('shipments/<int:pk>', views.ShipDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>', views.TransactionDetail.as_view()),
    path('requests/', views.RequestList.as_view()),
    path('requests/<int:pk>', views.RequestDetail.as_view()),
    path('transfers/', views.TransferList.as_view()),
    path('transfers/<int:pk>', views.TransferDetail.as_view()),
    path('issues/', views.IssueList.as_view()),
    path('issues/<int:pk>', views.IssueDetail.as_view()),
    path('vehicles/', views.VehicleList.as_view()),
    path('vehicles/<int:pk>', views.VehicleDetail.as_view()),
    path('employees/<int:pk>/worker', views.WorkerItemDetail.as_view()),
    path('employees/<int:pk>/worker/subsection', views.WorkerSubsections.as_view()),
    path('employees/<int:pk>/worker/subsection/<int:subid>/<int:itemid>', views.WorkerSubsectionDetail.as_view()),
    path('employees/<int:pk>/admin', views.AdminViewTransactionRequests.as_view()),
    path('employees/<int:pk>/admin/items', views.AdminItemsWarehouse.as_view()),
    path('employees/<int:pk>/admin/subsections', views.AdminSubsectionDetails.as_view()),
    path('employees/<int:pk>/admin/subsections/stores', views.AdminSubsectionItems.as_view()),
    path('employees/<int:pk>/admin/<int:wid>/<int:iid>', views.AdminTransactions.as_view()),
    path('employees/<int:pk>/exec/items/', views.ExecViewItems.as_view()),
    path('transactions/', views.ExecViewTransactions.as_view()),
    path('requests/', views.RequestList.as_view()),
    path('employees/<int:pk>/exec/requests/handle', views.ExecHandleRequests.as_view()),
]
