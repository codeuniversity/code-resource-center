from django.contrib import admin
from .models import Department, Institution, UserType, UserRole, UserProfile

admin.site.register(Department)
admin.site.register(Institution)
admin.site.register(UserType)
admin.site.register(UserRole)
admin.site.register(UserProfile)
