from django import forms
from .models import LearningResource

class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        fields = [
                'title',
                'url', 
                'description',
                'media_type',
                'department',
                'is_free',
        ]