from django import forms
from .models import *


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class Signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_number', 'street_name', 'city', 'state', 'zip_code']

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
        fields = ['item_description']

class RoomForm(forms.ModelForm):
     class Meta:
         model = Room
         fields = ['room_name','room_name']

