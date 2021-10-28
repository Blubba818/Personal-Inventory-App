from django import forms
from .models import Item, Room, Location


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'image', 'description', 'quantity', 'location_id']
        labels = {
            'name': 'Item Name',
            'image': 'Item Image',
            'description': 'Item Description',
            'quantity': 'Item Quantity',
            'location_id': 'Location'
        }


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'room_id']
        labels = {
            'name': 'Location Name',
            'room_id': 'Room'
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
        labels = {
            'name': 'Room Name'
        }
