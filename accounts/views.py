from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

 
def login_signup_view(request):
        if request.user.is_authenticated:
            return redirect('registrations:profile')
        if request.method == 'POST':
            form_login = AuthenticationForm(data=request.POST)
            form_signup = UserCreationForm(request.POST)
            if form_login.is_valid():
                user = form_login.get_user()
                login(request,user)
                return redirect('registrations:profile')
            if form_signup.is_valid():
                form_signup.save()
                return redirect('registrations:profile')            
        else:
            form_login = AuthenticationForm()
            form_signup = UserCreationForm()
        return render(request,'accounts/login.html',{'form_login':form_login, 'form_signup':form_signup})

# def signup_view(request):
#     if request.user.is_authenticated:
#         return redirect('registrations:profile')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('registrations:profile')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/sign_up.html', {'form_signup': form})


def logout_view(request):
    logout(request)
    return redirect('https://hackpcbt.tech')