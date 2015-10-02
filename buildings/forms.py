from django import forms
from .models import Building
from .models import Address

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['building_name', 'address_id', 'build_date']
