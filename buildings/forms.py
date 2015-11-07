from django import forms
from .models import *


class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['phone_number', 'start_date']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_number', 'street_name', 'city', 'state', 'zip_code']

    def clean_street_number(self):
        street_number = self.cleaned_data.get('street_number')
        if street_number == None:
            raise forms.ValidationError("Please enter a building name")
        return street_number

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['building_name', 'build_date', 'number_of_units']

    def clean_building_name(self):
        building_name = self.cleaned_data.get('building_name')
        if building_name == None:
            raise forms.ValidationError("Please enter a building name")
        return building_name

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['unit_number', 'parking_space', 'is_rented']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_description', ]

class ItemDetailsForm(forms.ModelForm):
    class Meta:
        model = Item_Detail
        fields = ['date', 'cost', 'vendor']

class RoomForm(forms.ModelForm):
     class Meta:
         model = Room
         fields = ['room_name']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name']
