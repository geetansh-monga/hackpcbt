from django import forms
from .models import user,team

class reg_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'mob', 'title', 'mail','dob','college','course','year','city','about',
                    'skills','githubUrl','linkedinUrl','team_id']
        widgets = {
            'dob': forms.SelectDateWidget,
        }


class team_form(forms.ModelForm):
    class Meta:
        model = team
        fields = '__all__'