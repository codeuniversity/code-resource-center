from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Profile

User = get_user_model()

###### REGISTER FORM FOR USERS ######
class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                "id":"password1",
                "class":"form-control",
                "placeholder":"Password",
                "name":"password1",               
            }
        )
    )
    password2 = forms.CharField(
        label='', 
        widget=forms.PasswordInput(
            attrs = {
                "id":"password2",
                "class":"form-control",
                "placeholder":"Repeat password",
                "name":"password2",               
            }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    "class":"form-control",
                    "id":"input-first-name",
                    "placeholder":"First name",
                    "name":"input-first-name",
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    "class":"form-control",
                    "id":"input-last-name",
                    "placeholder":"Last name",
                    "name":"input-last-name",
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    "class":"form-control",
                    "id":"input-email",
                    "placeholder":"Email",
                    "name":"input-email",
            }),
        }

    # sanitize form inputs
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # TO DO: Send email to users to confirm signup first
        # user.active = false
        if commit:
            user.save()
        return user

###### CREATE USER FORM FOR ADMINS ######
# source: Django documentation
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    # sanitize form inputs
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        # check if passwords match
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

###### CHANGE USER FORM FOR ADMINS ######
# source: Django documentation
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

###### UPDATE USER DETAILS FORMS ######
class UpdateUserForm(UserChangeForm):
    """A form for users to update their user info."""
            
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    "class":"form-control update-profile",
                    "name":"input-first-name",
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    "class":"form-control update-profile",
                    "name":"input-last-name",
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    "class":"form-control update-profile",
                    "name":"input-email",
                }
            ),
        }
        
    # sanitize form inputs
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name



    # def clean_password_confirm(self):
    #     # Check that the two password entries match
    #     password_confirm = self.cleaned_data.get("password_confirm")
    #     return password_confirm

    # def clean_password(self):
    #     """Regardless of what the user provides, return the initial value.
    #     This is done here, rather than on the field, because the
    #     field does not have access to the initial value"""
    #     return self.initial["password"]






# class UpdateUserForm(forms.ModelForm):
#  """A form for users to update their user accounts. In addition to the required
#     fields, it allows to update the password. The form adds an old password field, 
#     and a new and repeat new password field."""
#     old_password = forms.CharField(
#         label='', 
#         widget=forms.PasswordInput(
#             attrs = {
#                 "id":"old_password",
#                 "class":"form-control",
#                 "placeholder":"old password",
#                 "name":"old_password",               
#             }
#         )
#     )

#     new_password1 = forms.CharField(
#         label='', 
#         widget=forms.PasswordInput(
#             attrs = {
#                 "id":"new_password1",
#                 "class":"form-control",
#                 "placeholder":"New password",
#                 "name":"new_password1",               
#             }
#         )
#     )
#     new_password2 = forms.CharField(
#         label='', 
#         widget=forms.PasswordInput(
#             attrs = {
#                 "id":"new_password2",
#                 "class":"form-control",
#                 "placeholder":"Repeat new password",
#                 "name":"new_password2",               
#             }
#     ))

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#         labels = {
#             'first_name': '',
#             'last_name': '',
#             'email': ''
#         }
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs = {
#                     "class":"form-control",
#                     "id":"input-first-name",
#                     "placeholder":"First name",
#                     "name":"input-first-name",
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs = {
#                     "class":"form-control",
#                     "id":"input-last-name",
#                     "placeholder":"Last name",
#                     "name":"input-last-name",
#                 }
#             ),
#             'email': forms.EmailInput(
#                 attrs = {
#                     "class":"form-control",
#                     "id":"input-email",
#                     "placeholder":"Email",
#                     "name":"input-email",
#             }),
#         }

#     # sanitize form inputs
#     def clean_first_name(self):
#         first_name = self.cleaned_data['first_name']
#         return first_name
    
#     def clean_last_name(self):
#         last_name = self.cleaned_data['last_name']
#         return last_name

#     def clean_password2(self):
#         # Check that the password matches the old password
#         user = auth.authenticate(username=request.POST['email'], password=request.POST['old_password'])
#         if user is not None:
#         # Check that the two password entries match
#         new_password1 = self.cleaned_data.get("password1")
#         new_password2 = self.cleaned_data.get("password2")
#         # check if passwords match
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(RegisterForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         # TO DO: Send email to users to confirm signup first
#         # user.active = false
#         if commit:
#             user.save()
#         return user


###### PROFILE FORM ######
# source: Django documentation
# class ProfileCreationForm(forms.ModelForm):
    
#     class Meta:
#         model = Profile
#         fields = ('user_type', 'institution',)

        #  # Institution enums
        # CODE = 'CODE'
        # CD = 'CD'
        # OTHER = 'OTHER'
        # INSTITUTION_CHOICES = (
        #     (CODE, 'Code University'),
        #     (CD, 'Code+Design Camps'),
        #     (OTHER, 'other'),
        # )

        # # usertype enums
        # STUDENT = 'STUDENT'
        # AC_STAFF = 'AC_STAFF'
        # ADMIN_STAFF = 'ADMIN_STAFF'
        # ALUMNI = 'ALUMNI'
        # EXTERNAL = 'EXTERNAL'

        # USERTYPE_CHOICES = (
        #     (STUDENT, 'Student'),
        #     (CD, 'Code+Design Camper'),
        #     (AC_STAFF, 'Academic Staff'),
        #     (ADMIN_STAFF, 'Administrative Staff'),
        #     (ALUMNI, 'Alumni'),
        #     (EXTERNAL, 'External')
        # )
        # labels = {
        #     'user_type': 'What\'s your role at Code?',
        #     'institution': 'What\'s your organisation?',
        # }
        # widgets = {
        #     'user_type': forms.ChoiceField(
        #         choices = USERTYPE_CHOICES,
        #         attrs = {
        #             "class":"form-control",
        #             "id":"select-institution",
        #             "name":"select-institution",
        #         }

        #     ),

        # }

