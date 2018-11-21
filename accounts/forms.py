from django import forms
from .models import UserProfile

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'department',
            'user_type'
        ]