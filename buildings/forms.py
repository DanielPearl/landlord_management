from django import forms
from .models import Building
from .models import Address
from .models import Unit

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['building_name', 'address_id', 'build_date']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_number', 'parking_space', 'is_rented']