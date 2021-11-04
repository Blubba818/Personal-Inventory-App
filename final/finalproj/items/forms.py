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
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['name', 'image', 'room_id', 'description']
        labels = {
            'name': 'Location Name',
            'image': 'Location Image',
            'description': 'Location Description',
            'room_id': 'Room'
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'image', 'description']
        labels = {
            'name': 'Room Name',
            'image': 'Room Image',
            'description': 'Room Description'
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }
