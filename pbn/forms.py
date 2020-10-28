from django import forms
from .models import PBNsite


class NewPbn(forms.ModelForm):

    class Meta:
        model = PBNsite
        fields = '__all__'
