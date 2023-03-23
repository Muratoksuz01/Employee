from .models import ModelEmployee
from django import forms

class FormEmployee(forms.ModelForm): 
    class Meta:
        model=ModelEmployee
        fields=(
            "full_name",
            "mobile",
            "emp_code",
            "position",
        )
        labels={
            'full_name':'FULL Name',
            'emp_code':'EMP CODE'
        }
