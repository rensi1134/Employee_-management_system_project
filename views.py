from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from django.contrib import messages
from datetime import datetime
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emp = Employee.objects.all()
    context = {
        'emp' : emp
    }
    print(context)
    return render(request, 'view.html',context)


def add_emp(request): 
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        department = int(request.POST['department'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, department_id=department, role_id=role, hire_date=datetime.now())
        new_emp.save()
        # alert('Employee added successfully')
        emp = Employee.objects.all()
        context = {
        'emp' : emp
         }
        print(context)
        return render(request, 'view.html',context)
    
    elif request.method == 'GET':
        return render(request, 'add.html')
    
    else:
        return HttpResponse('404 ERROR!!! , Employee not added')


def remove_emp(request,emp_id = 0):
     if emp_id:
         try:
             emp_to_removed = Employee.objects.get(id=emp_id)
             emp_to_removed.delete()
            #  return HttpResponse('Employee removed successfully')
             emp = Employee.objects.all()
             context = {
                'emp' : emp
              }
             print(context)
             return render(request, 'view.html',context)
             
         except:
             return HttpResponse('Enter valid Employee ID')

     emp = Employee.objects.all()
     context = {
        'emp' : emp
         }
     
     return render(request, 'remove.html',context)


def edit_emp(request):
    if request.method == 'GET':
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        salary = int(request.GET['salary'])
        bonus = int(request.GET['bonus'])
        phone = int(request.GET['phone'])
        department = int(request.GET['department'])
        role = int(request.GET['role'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, department_id=department, role_id=role, hire_date=datetime.now())
        new_emp.save()
        # alert('Employee added successfully')
        emp = Employee.objects.all()
        context = {
        'emp' : emp
         }
        print(context)
        return render(request, 'view.html',context)
    
    elif request.method == 'POST':
        return render(request, 'edit.html')
    
    else:
        return HttpResponse('404 ERROR!!! , Employee not edited')



def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if department:
            emp = emp.filter(department__name__icontains = department )
        if role:
            emp = emp.filter(role__name__icontains = role )
        
        context = {
            'emp' : emp
        }
        return render(request,'view.html',context)
    elif request.method == 'GET':
        return render(request,'filter.html')
    else:
        return HttpResponse('404 ERROR')
    