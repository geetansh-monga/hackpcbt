from django.contrib import admin
from . import models

admin.site.register(models.user)
admin.site.register(models.team)
