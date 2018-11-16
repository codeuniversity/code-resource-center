from django.contrib import admin
from .models import Department, Institution, UserType

admin.site.register(Department)
admin.site.register(Institution)
admin.site.register(UserType)
