from django.urls import path,include
from . import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('employees/', views.EmployeeList.as_view()),
    path('employees/<int:pk>', views.EmployeeDetail.as_view()),
    path('drivers/', views.DriverList.as_view()),
    path('drivers/<int:pk>', views.DriverDetail.as_view()),
	path('routes/', views.RouteList.as_view()),
	path('warehouses/', views.WarehouseList.as_view()),
	path('warehouses/<int:pk>', views.WarehouseDetail.as_view()),
    path('items/', views.ItemList.as_view()),
	path('items/<int:pk>', views.ItemDetail.as_view()),
    path('worksat/', views.WorksList.as_view()),
    path('shipments/', views.ShipList.as_view()),
]
