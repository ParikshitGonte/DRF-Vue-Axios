from django.shortcuts import render
from .models import Employee

def EmployeeView(request):
    employees=Employee.objects.all()
    return render(request,'detail.html',{'employees':employees})

def EmployeeView1(request):
    employees=Employee.objects.all()
    return render(request,'demo.html',{'employees':employees})

def RestView(request):
    return render(request,'api_demo.html')