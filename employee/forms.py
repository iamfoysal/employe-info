from django import forms
from .models import Employee, Position, Gender

class employeeForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'} ))
    date_of_birth =forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    join_date =forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    
    class Meta:
        model = Employee 
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(employeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label ="Select"
        self.fields['gender'].empty_label= "Select"
        self.fields['position'].required = False 
        
        