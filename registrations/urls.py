from django.urls import path,include
from .views import profile,register

urlpatterns= [
    path('',profile),
    path('register/',register)
]