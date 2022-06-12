from django.contrib import admin
from employee.models import Position, Employee, Gender

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'emp_id', 'phone', 'position','join_date')


admin.site.register(Employee, EmployeeAdmin ) #call EmployeeAdmin this class show admin panel According to the form
admin.site.register( Position)
admin.site.register( Gender)
