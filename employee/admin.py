from django.contrib import admin
from employee.models import Position, Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'emp_id', 'phone', 'position','description','date')


admin.site.register(Employee, EmployeeAdmin ) #call EmployeeAdmin this class show admin panel According to the form
admin.site.register( Position)
