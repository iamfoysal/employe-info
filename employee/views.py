from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import employeeForm
from .models import Employee



def employee_info_list(request):
    context = {'employee_info_list': Employee.objects.all()}
    return render (request, "employee/index.html", context)



@login_required(login_url='signin')
def employee_info_form(request, id=0):
    if request.method == "GET":
        # form update section
        if id == 0:
            form = employeeForm()
        else: 
            employee = Employee.objects.get(pk=id)
            form = employeeForm(instance = employee)
        context = {"form" : form}
        return render (request, "employee/form.html", context)

    else: 
        if id ==0:
            form = employeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = employeeForm(request.POST,instance = employee)
        if form.is_valid(): #form validation check and save database
            form.save()
        return redirect('/')


        
def employee_info_view(request, pk):
    show = get_object_or_404(Employee, pk=pk)
    return render (request, "employee/view.html",{
        "show": show
    })
    

def employee_info_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/')

