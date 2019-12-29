from django.urls import path
from .views import profile,register_user,register_team

app_name = 'registrations'
urlpatterns= [
    path('',profile, name='profile'),
    path('register_user/',register_user,name='create_user'),
    path('register_team/',register_team,name='create_team'),
]