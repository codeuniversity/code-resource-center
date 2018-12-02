from django import forms
from .models import LearningResource, MediaType
from accounts.models import Department
from django.core.validators import URLValidator


class LearningResourceForm(forms.ModelForm):
    title = forms.CharField(
            widget = forms.TextInput(
                    attrs = {
                            'placeholder':'Title',
                            'class':'form-control',
                            }))
    url = forms.CharField(
            validators=[URLValidator()],
            widget=forms.TextInput(
                    attrs={
                            'placeholder':'URL',
                            'class':'form-control',
                            }))
    description = forms.CharField(
            required=False,
            widget=forms.Textarea(
                    attrs={
                            'placeholder':'Description',
                            'class':'form-control',
                            'rows': 4,
                            }))
    media_type = forms.ModelChoiceField(
            queryset=MediaType.objects.all(),
            widget=forms.Select(
                      attrs={'class':'form-control'}
            ))

    department = forms.ModelChoiceField(
            queryset=Department.objects.all(),
            widget=forms.Select(
                      attrs={'class':'form-control'}
            ))
#     department = forms.ModelMultipleChoiceField(
#             queryset=Department.objects.all(),
#             widget=forms.CheckboxSelectMultiple(
#                    attrs={'class':'form-control',}
#             ))
    is_free = forms.BooleanField(required=False)
    tag = forms.CharField(
            widget = forms.TextInput(
                    attrs = {
                            'placeholder':'Tags',
                            'class':'form-control',
                            }))


    class Meta:
        model = LearningResource
        fields = [
                'title',
                'url',
                'description',
                'media_type',
                'department',
                'is_free',
                'tag',
        ]
