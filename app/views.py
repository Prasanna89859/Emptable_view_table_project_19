from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def emptable(request):
    QLEMP=EmployeeTable.objects.all()
    d={'employeeTable':QLEMP}
    return HttpResponse(request,'emptable.html',d)

def emptable(request):
    en=input('Enter value: ')
    Job=input('Enter name: ')
    Mgr=input('Enter number: ')
    Hire=input('Enter Date: ')
    Sal=input('Enter Sal: ')
    Comm=input('Enter comm: ')
    Dept=input('Enter number: ')
    En=EmployeeTable.objects.get(Empo=en)[0]
    En.save()
    QLEMP=EmployeeTable.objects.get_or_create(EmployeeTable=en,Job=Job,Mgr=Mgr,Date=Hire,Sal=Sal,comm=Comm,Dept=Dept)[0]
    QLEMP.save()

    return HttpResponse('Emptable is create ')



