from django.shortcuts import render, redirect
from .models import Item, Room, Location
from .forms import ItemForm, LocationForm, RoomForm

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    location_list = Location.objects.all()
    room_list = Room.objects.all()
    context = {
        'item_list': item_list,
        'location_list': location_list,
        'room_list': room_list
    }
    return render(request, 'items/index.html', context)


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
    form = ItemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect('items:index')

    return render(request, 'items/item-form.html', {'form': form})


def create_location(request):
    form = LocationForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect('items:locations')

    return render(request, 'items/location-form.html', {'form': form})


def create_room(request):
    form = RoomForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect('items:rooms')

    return render(request, 'items/room-form.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('items:index')

    return render(request, 'items/item-form.html', {'form': form, 'item': item})


def update_location(request, id):
    location = Location.objects.get(id=id)
    form = LocationForm(request.POST or None, request.FILES or None, instance=location)

    if form.is_valid():
        form.save()
        return redirect('items:locations')

    return render(request, 'items/location-form.html', {'form': form, 'location': location})


def update_room(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(request.POST or None, request.FILES or None, instance=room)

    if form.is_valid():
        form.save()
        return redirect('items:rooms')

    return render(request, 'items/room-form.html', {'form': form, 'room': room})


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
        return redirect('items:index')

    return render(request, 'items/location-delete.html', {'location': location})


def delete_room(request, id):
    room = Room.objects.get(id=id)

    if request.method == 'POST':
        room.delete()
        return redirect('items:index')

    return render(request, 'items/room-delete.html', {'room': room})
