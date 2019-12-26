from django import forms
from .models import user,team

class reg_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','first_name' ,'last_name' ,'mob',
        'title','mail','dob','college','course','year','city' ,
        'about','skills','githubUrl','linkedinUrl','profile_pic', 
        ]


    