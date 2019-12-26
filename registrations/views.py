from django.shortcuts import render
from .models import user
from .registration_form import reg_form

# Create your views here.
def profile(request):
    user1 = user.objects.all()
    return render(request, 'registrations/profile.html',{'data' : user1})

def register(request):
    form = reg_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = reg_form()
    return render(request,'registrations/register.html',{'form' : form})    