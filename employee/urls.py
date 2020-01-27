from django.urls import path
from .views import *

urlpatterns = [
   path('',EmployeeView,name="EmployeeView"),
   path('list',EmployeeView1,name="EmployeeView1"),
   path('rest',RestView,name="RestView")
]