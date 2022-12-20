from django.shortcuts import render, HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def view_emp(request):
    emps=Employee.objects.all()
    context= {
        'emps':emps
    }  #acts as a dictionary

    # print(context)
    return render(request,'view_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        bonus=int(request.POST['bonus'])
        salary=int(request.POST['salary'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,phone=phone,role_id=role,dept_id=dept,bonus=bonus,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully!!")
        # print("POST")
    elif request.method=='GET':
        # print("GET")
        return render(request,'add_emp.html')
    else:
        return HttpResponse("LOL! An exception occured,pls solve it.")

def delete_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_tobe_removed=Employee.objects.get(id=emp_id)
            emp_tobe_removed.delete()
            return HttpResponse("Employee deleted successfully")
        except:
            return HttpResponse("Please Enter a valid Emp id")
    emps= Employee.objects.all()
    context={
        'emps': emps
    }
    return render(request,'delete_emp.html',context)


def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps= Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps= emps.filter(role__name__icontains=role)
        context= {
            'emps':emps
        }
        return render(request,'view_emp.html',context)

    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("Exception occured!")


