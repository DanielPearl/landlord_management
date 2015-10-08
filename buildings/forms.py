from django import forms
from .models import *

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['building_name', 'address_id', 'build_date']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_number', 'parking_space', 'is_rented']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['room_id','item_description']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name','room_name']