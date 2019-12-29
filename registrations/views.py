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
            return render(request,'registrations/profile.html',{'profile' : participants})
    else:
        return redirect('registrations:create_user')

@login_required(login_url='accounts:login_page')
def register_user(request):
    username = request.user.username
    form = reg_form(request.POST or None)
    if form.is_valid():
        tID = form.cleaned_data['team_id']
        teams = team.objects.filter(team_id = tID)
        for data in teams:
            tNAME = data.team_name
        details = user(
            username = username,
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            mob = form.cleaned_data['mob'],
            title = form.cleaned_data['title'],
            mail = form.cleaned_data['mail'],
            dob = form.cleaned_data['dob'],
            college = form.cleaned_data['college'],
            course = form.cleaned_data['course'],
            city = form.cleaned_data['city'],
            about = form.cleaned_data['about'],
            skills = form.cleaned_data['skills'],
            githubUrl = form.cleaned_data['githubUrl'],
            linkedinUrl = form.cleaned_data['linkedinUrl'],
            team_id = tID,
            teamname = tNAME
        )    
        details.save()
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