from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import employeeForm
from .models import Employee
# import io
# from reportlab.pdfgen import canvas  
# from django.http import HttpResponse  


# def employee_form_info_pdf(request):
#     pass


def employee_info_list(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Employee.objects.filter(Q(full_name__icontains=search) | Q(emp_id__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
        context =  { 'results': results, 'search': search}
        return render(request, 'employee/search-result.html', context)
  
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


# def search_result(request):
#     if request.method == 'POST':
#         search = request.POST.get('search')
#         results = Employee.objects.filter(Q(full_name__icontains=search) | Q(emp_id__icontains=search))
#         context =  { 'result': results, 'search': search}
#         return render(request, 'employee/search-result.html', context)