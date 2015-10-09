from django.conf.urls import include, url
from buildings import views

urlpatterns = [

# -------------------------------Forms----------------------------------
    # Building
    url(r'^building_form', views.building_form, name="building_form"),
    # Unit
    url(r'^units/unit_form/([\w\s]+)', views.unit_form, name="unit_form"),
    # Room
    url(r'^units/rooms/room_form/(?P<building_name>[\w\s]+)/(?P<unit_number>[\d]+)', views.room_form, name="room_form"),
    # Item
    url(r'^item_form', views.item_form, name="item_form"),

# -------------------------------Pages----------------------------------

    #Building
    url(r'^$', views.buildings, name="buildings"),
    #Room
    url(r'^units/rooms/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)', views.rooms, name="rooms"),
    #Unit
    url(r'^units/(?P<building_name>[\w\s]+)', views.units, name="units"),


]
