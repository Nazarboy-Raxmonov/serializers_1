from django.contrib import admin
from .models import StaffModels, UsersModels

# Register your models here.
admin.site.register(StaffModels)
admin.site.register(UsersModels)
