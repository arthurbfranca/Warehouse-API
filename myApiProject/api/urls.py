from django.urls import path,include
from . import views
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('employees/', views.EmployeeList.as_view()),
]
