from django.urls import path
from .views import website_view

app_name = 'website'
urlpatterns = [
    path('',website_view,name='main_website')
]