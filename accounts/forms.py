from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile

# inherits from Django's UserCreationForm 
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # first_name = forms.CharField(required=True)
    # last_name = forms.CharField(required=True)

    class Meta: 
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        # sanitize form input
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.last_name = self.cleaned_data['email']

        if commit:
            user.save()

        return user
