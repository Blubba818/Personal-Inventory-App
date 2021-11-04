from . import views
from django.urls import path

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('location', views.locations, name='locations'),
    path('room', views.rooms, name='rooms'),
    path('sort/<sort_by>', views.index_sorted, name='index_sorted'),
    path('location/sort/<sort_by>', views.locations_sorted, name='locations_sorted'),
    path('<int:item_id>', views.item_detail, name='item_detail'),
    path('location/<int:item_id>', views.location_detail, name='location_detail'),
    path('room/<int:item_id>', views.room_detail, name='room_detail'),
    path('add', views.create_item, name='create_item'),
    path('update/<int:id>', views.update_item, name='update_item'),
    path('delete/<int:id>', views.delete_item, name='delete_item'),
    path('location/add', views.create_location, name='create_location'),
    path('location/update/<int:id>', views.update_location, name='update_location'),
    path('location/delete/<int:id>', views.delete_location, name='delete_location'),
    path('room/add', views.create_room, name='create_room'),
    path('room/update/<int:id>', views.update_room, name='update_room'),
    path('room/delete/<int:id>', views.delete_room, name='delete_room'),
]
