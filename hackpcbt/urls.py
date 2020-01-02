from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrations/',include('registrations.urls')),
    path('',include('accounts.urls'))
]
