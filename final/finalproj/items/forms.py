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
        fields = ['name', 'image', 'room_id']
        labels = {
            'name': 'Location Name',
            'image': 'Location Image',
            'room_id': 'Room'
        }


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'image']
        labels = {
            'name': 'Room Name',
            'image': 'Room Image'
        }
