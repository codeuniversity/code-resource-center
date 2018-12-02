from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.files.images import get_image_dimensions
from .models import Profile, Department, ProfileDepartment

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
        if not first_name:
             raise forms.ValidationError("First name is empty.")
        if not first_name.replace(" ", "").replace("-", "").replace(".", "").isalpha():
            raise forms.ValidationError("First name contains invalid characters.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name:
            raise forms.ValidationError("Last name is empty.")
        if not last_name.replace(" ", "").replace("-", "").replace(".", "").isalpha():
            raise forms.ValidationError("Last name contains invalid characters.")
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
                    "placeholder": "First name",
                    "name":"input-first-name",
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    "class":"form-control update-profile",
                    "placeholder": "Last name",
                    "name":"input-last-name",
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    "class":"form-control update-profile",
                    "placeholder": "Email",
                    "name":"input-email",
                }
            ),
        }

    # sanitize form inputs
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name:
             raise forms.ValidationError("First name is empty.")
        if not first_name.replace(" ", "").replace("-", "").replace(".", "").isalpha():
            raise forms.ValidationError("First name contains invalid characters.")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        # check if passwords match
        if not last_name:
            raise forms.ValidationError("Last name is empty.")
        if not last_name.replace(" ", "").replace("-", "").replace(".", "").isalpha():
            raise forms.ValidationError("Last name contains invalid characters.")
        return last_name

###### PROFILE FORM ######
class ProfileChangeForm(forms.ModelForm):
    """A form for users to change their profile information."""

    class Meta:
        model = Profile
        fields = ('avatar',)

    # TO DO: Image validation
    #  source: 
    # https://stackoverflow.com/questions/6396442/add-image-avatar-field-to-users-in-django
    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            width, height = get_image_dimensions(avatar)

            # validate dimensions
            max_width = 6000
            max_height = 6000
            if int(width) > max_width or int(height) > max_height:
                raise forms.ValidationError( u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'gif', 'png']):
                raise forms.ValidationError('Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(avatar) > (10000 * 1024):
                raise forms.ValidationError('Avatar file size may not exceed 10Mb.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar

###### CHANGE PROFILE_DEPARTMENT FORM ######
class ProfileDepartmentChangeForm(forms.ModelForm):

    class Meta:
        model = ProfileDepartment
        fields = ('department',)