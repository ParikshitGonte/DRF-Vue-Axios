from django.shortcuts import render
from .models import Employee
from django.core import serializers

def EmployeeView(request):
    employee=serializers.serialize("json",Employee.objects.all())
    return render(request,'detail.html',{'employee':employee})

def EmployeeView1(request):
    employee=serializers.serialize("json",Employee.objects.all())
    return render(request,'demo.html',{'employee':employee})

def RestView(request):
    return render(request,'api_demo.html')