from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

 
def login_view(request):
        if request.user.is_authenticated:
            return redirect('registrations:profile')
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request,user)
                return redirect('registrations:profile')
        else:
            form = AuthenticationForm()
        return render(request,'accounts/login.html',{'form':form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('registrations:profile')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrations:profile')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('website:main_website')