from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import user,team
from .registration_form import reg_form,team_form


@login_required(login_url='accounts:login_page')

def profile(request):
    username = request.user.username
    user1 = user.objects.all()
    for users in user1:
        if users.username == username:
            return render(request, 'registrations/profile.html',{'data' : user1,'user' : username})
    else:
        return redirect('registrations:create_user')

@login_required(login_url='accounts:login_page')
def register_user(request):
    username = request.user.username
    form = reg_form(request.POST or None)
    if form.is_valid():    
        mobile_no = form.cleaned_data.get("mob")
        teamId = form.cleaned_data.get("team_id")
        form.save()
        obj_user = user.objects.get(mob = mobile_no)
        obj_team = team.objects.get(team_id = teamId )
        obj_user.username = username
        obj_user.teamname = obj_team.team_name
        obj_user.save()
        return redirect('registrations:profile')
    else:
        form = reg_form()
    return render(request,'registrations/form.html',{'form' : form}) 

def register_team(request):
    form = team_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registrations:profile')
    else:
        form = team_form()
    return render(request,'registrations/create_team.html',{'team_form' : team_form})