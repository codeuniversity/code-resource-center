from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

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
                "id":"input-userame",
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
        required=True,
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
            'password'
        )

    def clean_fname(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        # if not "max" in first_name:
        #     raise forms.ValidationError("This is not a valid first name.")
        return  first_name
    
    def clean_lname(self, *args, **kwargs):
        last_name = self.cleaned_data.get("last_name")
        return  last_name

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        return  username

    # allow only @code.berlin emails to sign up 
    def valid_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("@code.berlin"):
            raise forms.ValidationError("This is not a valid email. Please contact administrator.")
        return email
    
    # Password must match
    def password_match(self, *args, **kwargs):
        password = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password == password2:
            raise forms.ValidationError("Passwords must match.")
        return password