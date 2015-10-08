from django.conf.urls import include, url
from buildings import views

urlpatterns = [

# -------------------------------Building----------------------------------
    #  Page
    url(r'^$', views.buildings, name="buildings"),
    #  Form
    url(r'^building_form', views.building_form, name="building_form"),

# -------------------------------Units----------------------------------
    #  Page
    url(r'^units/(?P<building_name>[\w\s]+)', views.units, name="units"),
    #  Form
    url(r'^units/unit_form/([\w\s]+)', views.unit_form, name="unit_form"),

# -------------------------------Rooms----------------------------------
    #  Page
    url(r'^units/rooms/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s]+)', views.rooms, name="rooms"),
    #  Form
    url(r'^units/rooms/room_form/([\w\s]+)', views.room_form, name="room_form"),

# -------------------------------Building----------------------------------
    #  Form
    url(r'^item_form', views.item_form, name="item_form"),
]
