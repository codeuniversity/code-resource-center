from django import forms
from .models import LearningResource, MediaType
from accounts.models import Department
from django.core.validators import URLValidator
from django.forms.widgets import CheckboxSelectMultiple



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
                      attrs={
                              'class':'form-control',
                      }))
                # Note that if a ModelChoiceField is required and has a default initial value, no empty choice is created (regardless of the value of empty_label).
                # todo 

         
#     department = forms.ModelChoiceField(
#             queryset=Department.objects.all(),
#             widget=forms.Select(
#                       attrs={'class':'form-control'}
#             ))
    department = forms.ModelMultipleChoiceField(
            queryset=Department.objects.all(),
            widget=forms.CheckboxSelectMultiple(
                   attrs={}
            ))
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

        def __init__(self, *args, **kwargs):
        
                super(LearningResourceForm, self).__init__(*args, **kwargs)
                
                self.fields["department"].widget = CheckboxSelectMultiple()
                self.fields["department"].queryset = Department.objects.all()
