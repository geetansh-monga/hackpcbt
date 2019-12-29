from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import user,team
from .registration_form import reg_form,team_form


@login_required(login_url='accounts:login_page')

def profile(request):
    username = request.user.username
    profiles = user.objects.all()
    for participants in profiles:
        if participants.username == username:
            return render(request,'registrations:profile',{'profile' : participants})
    else:
        return redirect('registrations:create_user')

@login_required(login_url='accounts:login_page')
def register_user(request):
    username = request.user.username
    form = reg_form(request.POST or None)
    if form.is_valid():    
        form.save()
        # obj_user = user.objects.get(mob = mobile_no)
        # obj_user.username = username
        # obj_user.save(['username'])
        return redirect('registrations:profile')
    else:
        form = reg_form()
    return render(request,'registrations/form.html',{'form' : form}) 

@login_required(login_url='accounts:login_page')
def register_team(request):
    form = team_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registrations:create_user')
    else:
        form = team_form()
    return render(request,'registrations/create_team.html',{'team_form' : team_form})