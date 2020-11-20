from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib.auth.admin import UserAdmin

UserAdmin.fieldsets += ('Profile Fields', {'fields': ('description', 'profile_picture', 'birth_date','slug')}),
admin.site.register(User, UserAdmin)
