from django.urls import path
from . import views

urlpatterns = [
    path("", views.employee_info_list, name= "employee_info_list_insert"),
    path("form/", views.employee_info_form, name="employee_form"),
    path("<int:id>/",views.employee_info_form, name= "employee_info_update"),
    path("view/<int:pk>/", views.employee_info_view, name ="views_info"),
    
    path("delete/<int:id>/", views.employee_info_delete, name="employee_delete"),

    # path("delete_confirm/<int:pk>/", views.delete_confirm, name="confirm_delete"),

    
]