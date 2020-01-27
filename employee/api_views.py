from rest_framework import viewsets
from .serializers import EmployeeSerializer
from .models import *

class EmployeeView(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

    

