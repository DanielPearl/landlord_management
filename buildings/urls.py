from django.conf.urls import include, url
from buildings import views

# urlpatterns = [
#
# # -------------------------------Forms----------------------------------
#     # Building form
#     url(r'^building_form', views.building_form, name="building_form"),
#     # Unit form
#     url(r'^units/unit_form/([\w\s]+)', views.unit_form, name="unit_form"),
#     # Room form
#     url(r'^units/rooms/room_form/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)', views.room_form, name="room_form"),
#     # Item form
#     url(r'^units/rooms/items/item_form/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)/(?P<room_name>[\w\s\d]+)', views.item_form, name="item_form"),
#     # Item form
#     url(r'^units/rooms/items/item_details/item_details_form/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)/(?P<room_name>[\w\s\d]+)/(?P<item_description>[\w\s\d]+)', views.item_details_form, name="item_details_form"),
#
# # -------------------------------Pages----------------------------------
#     #Item details page
#     url(r'^units/rooms/items/item_details/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)/(?P<room_name>[\w\s\d]+)/(?P<item_description>[\w\s\d]+)',
#         views.item_details, name="item_details"),
#     #Items page
#     url(r'^units/rooms/items/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)/(?P<room_name>[\w\s\d]+)', views.items, name="items"),
#     #Room page
#     url(r'^units/rooms/(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)', views.rooms, name="rooms"),
#     #Unit page
#     url(r'^units/(?P<building_name>[\w\s]+)', views.units, name="units"),
#
#     #Building page
#     # url(r'^buildings/', views.buildings, name="buildings"),
#
#     #Building/Homepage
#     url(r'^$', views.buildings, name="buildings"),
#     #Register page
#     url(r'^register', views.register_form, name="register")
#
# ]

urlpatterns = [

# -------------------------------Forms----------------------------------
    # Building form
    url(r'^building_form', views.building_form, name="building_form"),
    # Unit form
    url(r'^([\w\s]+)/unit_form/', views.unit_form, name="unit_form"),
    # Room form
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)/room_form/', views.room_form, name="room_form"),
    # Item form
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)/(?P<room_name>[\w\s\d]+)/item_form/', views.item_form, name="item_form"),
    # Item form
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\d]+)/(?P<room_name>[\w\s\d]+)/(?P<item_description>[\w\s\d]+)/item_details_form/', views.item_details_form, name="item_details_form"),

# -------------------------------Pages----------------------------------
    #Item details page
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)/(?P<room_name>[\w\s\d]+)/(?P<item_description>[\w\s\d]+)',
        views.item_details, name="item_details"),
    #Items page
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)/(?P<room_name>[\w\s\d]+)', views.items, name="items"),
    #Room page
    url(r'^(?P<building_name>[\w\s]+)/(?P<unit_number>[\w\s\d]+)', views.rooms, name="rooms"),
    #Unit page
    url(r'^(?P<building_name>[\w\s]+)', views.units, name="units"),

    #Building page
    # url(r'^buildings/', views.buildings, name="buildings"),

    #Building/Homepage
    url(r'^$', views.buildings, name="buildings"),
    #Register page
    url(r'^register', views.register_form, name="register")

]
