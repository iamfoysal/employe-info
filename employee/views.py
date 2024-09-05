from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import employeeForm
from .models import *
from django.contrib import messages
# import io
# from reportlab.pdfgen import canvas  
# from django.http import HttpResponse  


# def employee_form_info_pdf(request):
#     pass


def employee_info_list(request):
    employee = Employee.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        results = Employee.objects.filter(Q(full_name__icontains=search) | Q(emp_id__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
        context =  { 'results': results, 'search': search}
        return render(request, 'employee/search-result.html', context)
  
    context = {'employee_info_list': employee }
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
    

## use for modal

# def employee_info_delete(request, pk):
#     employee = Employee.objects.get(pk=pk)
#     employee.delete()
#     return redirect('/')



def delete_confirm(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('/')
    context ={'employee': employee}
    return render (request, 'employee/delete.html', context)





def add_employee(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        emp_id = request.POST.get('emp_id')
        position_id = request.POST.get('position')
        join_date = request.POST.get('join_date')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        gender_id = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        description = request.POST.get('description')

        position = Position.objects.get(id=position_id)
        gender = Gender.objects.get(id=gender_id)

        Employee.objects.create(
            full_name=full_name,
            fathers_name=fathers_name,
            mothers_name=mothers_name,
            emp_id=emp_id,
            position=position,
            join_date=join_date,
            phone=phone,
            email=email,
            gender=gender,
            date_of_birth=date_of_birth,
            address=address,
            description=description
        )
        print("request.POST", request.POST)
        messages.success(request, 'Employee added successfully')
        return redirect('/')  

    positions = Position.objects.all()
    genders = Gender.objects.all()

    return render(request, 'employee/employee_form.html', {'positions': positions, 'genders': genders})

















from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Webhook
import json



@csrf_exempt
def webhook_view(request):
    if request.method == 'POST':
        try:
            response = json.loads(request.body)
            webhook = Webhook(receive_response=response)
            webhook.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)})
    return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})



def list_webhooks(request):
    if request.method == 'GET':
        webhooks = Webhook.objects.all()
        response = []
        for webhook in webhooks:
            response.append({
                'id': webhook.id,
                'receive_response': webhook.receive_response,
                'created_at': webhook.created_at,
                'updated_at': webhook.updated_at
            })
        return JsonResponse(response, safe=False)
    return JsonResponse({'status': 'failed', 'error': 'Invalid request method'})