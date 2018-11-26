from django import forms
from .models import LearningResource, MediaType
from accounts.models import Department
from django.core.validators import URLValidator


class LearningResourceForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Title'}))
    url         = forms.CharField(validators=[URLValidator()], widget=forms.TextInput(attrs={'placeholder':'URL'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder':'Description'}))
    media_type  = forms.ModelChoiceField(queryset=MediaType.objects.all())
    department  = forms.ModelChoiceField(queryset=Department.objects.all())
    is_free     = forms.BooleanField(required=False)
    tag         = forms.CharField()

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

#     pub_date = models.DateTimeField(auto_now_add=True)
#     votes_total = models.IntegerField(default=1)
#     last_edit_date = models.DateTimeField(auto_now_add=True)