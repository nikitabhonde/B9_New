# step 2) Create forms.py file inside your app

from django.forms import fields
from cbv_app.models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee                    # To specify the model to be used to create form  
        fields = '__all__'                  # It includes all the fields of model  