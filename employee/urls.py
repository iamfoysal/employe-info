from django.urls import path
from . import views



urlpatterns = [
   
]
urlpatterns = [
    path("", views.employee_info_list, name= "employee_info_list_insert"),
    path("form/", views.employee_info_form, name="employee_form"),
    path("<int:id>/",views.employee_info_form, name= "employee_info_update"),
    path("view/<int:pk>/", views.employee_info_view, name ="views_info"),
    path("delete_confirm/<int:pk>/", views.delete_confirm, name="confirm_delete"),
    path('add_employee/', views.add_employee, name='add_employee'),
    # path("delete/<int:pk>/", views.employee_info_delete, name="employee_delete"),
    # path("pdf/", views.employee_form_info_pdf, name="employee_form_info_pdf"),
    path("infobip-webhook/", views.webhook_view, name='infobip-webhook'),
    path('hook-list/', views.list_webhooks, name='list_webhooks'),
]