from django import forms
from .models import Employee

class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

# def __init__(self, *args, **kwargs):
#     siper(employeeForm,self).__init__(*args, **kwargs)
#     self.fields['position'].empty_lable ="Select"
#     self.fields['position'].required = False 
    
        