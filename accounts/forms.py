from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserProfile

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

###### CHANGE USER FORM ######
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


class UserSignupForm(forms.ModelForm):
    first_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"input-first-name",
                "placeholder":"first name",
                "name":"input-first-name",
            }
        )
    )
    last_name = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"input-last-name",
                "placeholder":"last name",
                "name":"input-last-name",
            }
        )
    )
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "id":"input-username",
                "placeholder":"username",
                "name":"input-username",
            }
        )
    )
    email = forms.EmailField(
        label='',
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "id":"input-email",
                "placeholder":"email",
                "name":"input-email",
            }
        )    
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "id":"password1",
                "class":"form-control",
                "placeholder":"password",
                "name":"password1",
            }
        )
    )
    password2 = forms.CharField(
        # required=True,
        widget=forms.PasswordInput(
            attrs={
                "id":"password2",
                "class":"form-control",
                "placeholder":"repeat password",
                "name":"password2",
            }
        )
    )
    class Meta: 
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    def clean_fname(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        if not "max" in first_name:
            raise forms.ValidationError("This is not a valid first name.")
        return self.first_name
    
    # def clean_lname(self, *args, **kwargs):
    #     last_name = self.cleaned_data.get("last_name")
    #     return self.last_name

    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")
    #     return self.username

    # allow only @code.berlin emails to sign up 
    def valid_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("@code.berlin"):
            raise forms.ValidationError("This is not a valid email. Please contact administrator.")
        return self.email
    
    # Password must match
    def password_match(self, *args, **kwargs):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords must match.")
        return self.password2
    
    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=False)
        # sanitize form input
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
