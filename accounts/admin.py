from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Department, Institution, UserType, UserRole, UserProfile
from .forms import UserCreationForm, UserChangeForm

# load custom user model
User = get_user_model()

###### ADD & CHANGE USERS IN ADMIN ######
# source: Django documentation
class UserAdmin(BaseUserAdmin):
    # Search tool allows admin to search by email
    search_fields = ['email', 'first_name', 'last_name']
    # forms to UPDATE user instance
    form = UserChangeForm 
    # form to CREATE user instance
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Register models in admin
admin.site.register(User, UserAdmin)

# admin.site.register(UserManager)
admin.site.register(Department)
admin.site.register(Institution)
admin.site.register(UserType)
admin.site.register(UserRole)
admin.site.register(UserProfile)
