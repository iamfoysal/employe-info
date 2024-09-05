from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from employee.models import Position, Employee, Gender, Webhook




class PositionAdmin(ImportExportModelAdmin):

    list_display = ('title',)
    search_fields = ('title',)
    # ordering = ('created_at',)
    list_per_page = 20

    class Meta:
        model = Position
  
class EmployeeAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'emp_id', 'phone', 'position','join_date')
    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin ) #call EmployeeAdmin this class show admin panel According to the form
# admin.site.register( Position, PositionResource)
admin.site.register(Position, PositionAdmin)
admin.site.register( Gender)

class WebhookAdmin(admin.ModelAdmin):
    list_display = ['id','receive_response', 'created_at', 'updated_at']
  
    list_per_page = 100

admin.site.register(Webhook, WebhookAdmin)  