from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Item, Room, Location
from .forms import ItemForm, LocationForm, RoomForm

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'items/index.html', context)


def about(request):
    return render(request, 'items/about.html')


def locations(request):
    location_list = Location.objects.all()
    room_list = Room.objects.all()
    context = {
        'location_list': location_list,
        'room_list': room_list
    }
    return render(request, 'items/locations.html', context)


def rooms(request):
    room_list = Room.objects.all().order_by('name')
    context = {
        'room_list': room_list,
    }
    return render(request, 'items/rooms.html', context)


def index_sorted(request, sort_by):
    item_list = Item.objects.all().order_by(sort_by)
    context = {
        'item_list': item_list,
    }
    return render(request, 'items/index.html', context)


def locations_sorted(request, sort_by):
    location_list = Location.objects.all().order_by(sort_by)
    context = {
        'location_list': location_list,
    }
    return render(request, 'items/locations.html', context)


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'items/item-detail.html', context)


def location_detail(request, item_id):
    location = Location.objects.get(pk=item_id)
    context = {
        'location': location
    }
    return render(request, 'items/location-detail.html', context)


def room_detail(request, item_id):
    room = Room.objects.get(pk=item_id)
    context = {
        'room': room
    }
    return render(request, 'items/room-detail.html', context)


def create_item(request):
    item_form = ItemForm(request.POST or None, request.FILES or None)

    if item_form.is_valid():
        item_form.instance.created_by = request.user
        item_form.save()
        return redirect('items:index')

    return render(request, 'items/item-form.html', {'item_form': item_form})


def create_location(request):
    location_form = LocationForm(request.POST or None, request.FILES or None)

    if location_form.is_valid():
        location_form.instance.created_by = request.user
        location_form.save()
        return redirect('items:create_item')

    return render(request, 'items/location-form.html', {'location_form': location_form})


def create_room(request):
    room_form = RoomForm(request.POST or None, request.FILES or None)

    if room_form.is_valid():
        room_form.instance.created_by = request.user
        room_form.save()
        return redirect('items:create_location')

    return render(request, 'items/room-form.html', {'room_form': room_form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    item_form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if item_form.is_valid():
        item_form.save()
        return redirect('items:index')

    return render(request, 'items/item-form.html', {'item_form': item_form, 'item': item})


def update_location(request, id):
    location = Location.objects.get(id=id)
    location_form = LocationForm(request.POST or None, request.FILES or None, instance=location)

    if location_form.is_valid():
        location_form.save()
        return redirect('items:locations')

    return render(request, 'items/location-form.html', {'location_form': location_form, 'location': location})


def update_room(request, id):
    room = Room.objects.get(id=id)
    room_form = RoomForm(request.POST or None, request.FILES or None, instance=room)

    if room_form.is_valid():
        room_form.save()
        return redirect('items:rooms')

    return render(request, 'items/room-form.html', {'room_form': room_form, 'room': room})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('items:index')

    return render(request, 'items/item-delete.html', {'item': item})


def delete_location(request, id):
    location = Location.objects.get(id=id)

    if request.method == 'POST':
        location.delete()
        return redirect('items:locations')

    return render(request, 'items/location-delete.html', {'location': location})


def delete_room(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('items:rooms')

    return render(request, 'items/room-delete.html', {'room': room})
