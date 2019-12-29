from django import forms
from .models import user,team
from django.forms.widgets import DateInput

class reg_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'mob', 'title', 'mail','dob','college','course','year','city','about',
                    'skills','githubUrl','linkedinUrl','team_id']
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


class team_form(forms.ModelForm):
    class Meta:
        model = team
        fields = '__all__'