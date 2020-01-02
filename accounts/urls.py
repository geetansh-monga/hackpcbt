from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.login_signup_view,name='login_page'),
    # path('signup/',views.signup_view,name='signup_page'),
    path('logout/',views.logout_view,name='logout_page'),
]