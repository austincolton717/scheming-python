from django import forms
from .models import seoProject


class newProject(forms.ModelForm):

    class Meta:
        model = seoProject
        fields = '__all__'
