from django import forms
from .models import user,team

class reg_form(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'
        widgets = {
            'dob': forms.SelectDateWidget,
        }



    