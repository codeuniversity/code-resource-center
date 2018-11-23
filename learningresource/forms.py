from django import forms
from .models import LearningResource, MediaType
from accounts.models import Department

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

class RawResourceForm(forms.Form):
    title       = forms.CharField()
    url         = forms.CharField()
    description = forms.CharField(required=False, widget=forms.Textarea)
    media_type  = forms.ModelChoiceField(queryset=MediaType.objects.all())
    department  = forms.ModelChoiceField(queryset=Department.objects.all())
    is_free     = forms.BooleanField(required=False)
