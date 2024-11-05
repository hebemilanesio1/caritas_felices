# appprueba/forms.py

from django import forms
from .models import CampanaActiva

class CampanaForm(forms.ModelForm):
    class Meta:
        model = CampanaActiva
        fields = ['campaign_name', 'description', 'campaign_image']
