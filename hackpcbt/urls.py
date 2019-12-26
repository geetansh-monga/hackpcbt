from django.contrib import admin
from django.urls import path,include
from website import views as main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_view.website),
    path('register/',include('registrations.urls'))
]
