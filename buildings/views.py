from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

"""---------------------------------------------------------------------------
                                Authentication
---------------------------------------------------------------------------"""


def login_user(request):
    """
    :param request:
    :return login form:
    """
    logout_user(request)

    # login form submitted
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # user authentication for username & password
        user = authenticate(username=username, password=password)

        # If user is registered
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/buildings/')
        else:
            return HttpResponse("Invalid login info")
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/buildings/')
        else:
            return render(request, 'homepage.html')


def register_form(request):
    """
    :param request:
    :return register form:
    """
    register_title = "Register"
    registered = False

    # if form is submitted, save user and manager info
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        manager_form = ManagerForm(data=request.POST)

        # if user and manager fields are valid
        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            manager = manager_form.save(commit=False)
            manager.user = user
            manager.save()
            registered = True

            username = request.POST.get('username')
            password = request.POST.get('password')

            # user authentication for username & password
            user = authenticate(username=username, password=password)

        # If user is registered
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/buildings/")  # return to building page
        else:
            print(user_form.errors, manager_form.errors)
    else:
        user_form = UserForm()
        manager_form = ManagerForm()

    context = {
        'register_title': register_title,
        'user_form': user_form,
        'manager_form': manager_form,
        'registered': registered
    }
    return render(request, 'register_form.html', context)


def logout_user(request):
    """
    :param request:
    :return logout form:
    """
    logout(request)
    return HttpResponseRedirect('/')


"""---------------------------------------------------------------------------
                                Page Renders
---------------------------------------------------------------------------"""


def buildings(request):
    """
    :param request
    :return buildings page
    """

    if request.user.is_authenticated():
        title = "Buildings"

        # forms saved
        building_form = BuildingForm()
        address_form = AddressForm()

        # query filter
        buildings = Building.objects.filter(manager_id__user=request.user)

        # building page title
        name = request.user.first_name + " " + request.user.last_name

        # Dictionary keys to be used in templates
        context = {
            "title": title,
            "manager_name": name,
            "buildings": buildings,
            "building_form": building_form,
            "address_form": address_form
        }
        return render(request, 'buildings.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')


def units(request, building_name):
    """
    :param request, building name & unit #:
    :return unit page:
    """

    if request.user.is_authenticated():

        # unit page title
        units = Unit.objects.filter(building_id__manager_id__user=request.user,
                                    building_id__building_name=building_name)

        # query filter
        context = {
            "units": units,
            "building_name": building_name,
        }
        return render(request, 'units.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')


def rooms(request, building_name, unit_number):
    """
    :param building name & unit #:
    :return room page:
    """

    if request.user.is_authenticated():

        # room page title
        title = building_name + " >  #" + unit_number

        # query filter
        rooms = Room.objects.filter(unit_id__building_id__manager_id__user=request.user,
                                    unit_id__unit_number=unit_number,
                                    unit_id__building_id__building_name=building_name)

        # Dictionary keys to be used by templates
        context = {
            "title": title,
            "rooms": rooms,
            "building_name": building_name,
            "unit_number": unit_number,
        }
        return render(request, 'rooms.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')


def items(request, building_name, unit_number, room_name):
    """
    :param request, building name, unit, room name:
    :return items page:
    """

    if request.user.is_authenticated():

        # item page title
        title = building_name + " >  #" + unit_number + " >  " + room_name

        # query filter
        items = Item.objects.filter(room_id__unit_id__building_id__manager_id__user=request.user,
                                    room_id__room_name=room_name,
                                    room_id__unit_id__unit_number=unit_number,
                                    room_id__unit_id__building_id__building_name=building_name)

        # Dictionary keys to be used by templates
        context = {
            "items": items,
            "item_title": title,
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name,
        }
        return render(request, 'items.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')


def item_details(request, building_name, unit_number, room_name, item_description):
    """
    :param request, building_name, unit #, room name:
    :return item form page:
    """

    if request.user.is_authenticated():

        # sets name equal to name attribute in item detail model
        title = building_name + " >  #" + unit_number + " >  " + room_name + " >  " + item_description

        # sets list to everything saved in item detail object
        item_details = Item_Detail.objects.filter(item_id__room_id__unit_id__building_id__manager_id__user=request.user,
                                                  item_id__item_description=item_description,
                                                  item_id__room_id__room_name=room_name,
                                                  item_id__room_id__unit_id__unit_number=unit_number,
                                                  item_id__room_id__unit_id__building_id__building_name=building_name)

        context = {  # Dictionary used by template
                     "item_details": item_details,
                     "item_detail_title": title,
                     "building_name": building_name,
                     "unit_number": unit_number,
                     "room_name": room_name,
                     "item_description": item_description
        }
        return render(request, 'item_details.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')


"""---------------------------------------------------------------------------
                                Forms
---------------------------------------------------------------------------"""



def building_form(request):
    """
    :param request:
    :return building form page:
    """

    building_title = "Add Building"

    building_form = BuildingForm()
    address_form = AddressForm()

    # form submitted
    if request.method == 'POST':
        building_form = BuildingForm(request.POST)
        address_form = AddressForm(request.POST)

        # form valid
        if building_form.is_valid() and address_form.is_valid():
            address = address_form.save()

            building = building_form.save(commit=False)
            building.address_id = address
            building.save()

            # If no buildings exist in the database
            if building.number_of_units > 0:
                for i in range(building.number_of_units):

                    # Create unit
                    unit = Unit()
                    unit.unit_number = i + 1
                    unit.building_id = building
                    unit.is_rented = False
                    unit.parking_space = "no parking"
                    unit.save()

                    # Create bedroom
                    bedroom = create_room(request, unit, room_type='bedroom')
                    create_bedroom_items(request, bedroom)

                    # Create kitchen
                    kitchen = create_room(request, unit, room_type='kitchen')
                    create_kitchen_items(request, kitchen)

                    # Create bathroom
                    bathroom = create_room(request, unit, room_type='bathroom')
                    create_bathroom_items(request, bathroom)

            # query get
            username = Manager.objects.get(user=request.user)
            building.manager_id.add(username)
            building.save()  # save input into database

            return HttpResponseRedirect("/buildings/")  # return to building page
        else:
            return HttpResponse("Invalid login info")
            # raise forms.ValidationError("Please enter something")
            # raise ValidationError(_('Invalid value%(value)s'),code="invalid",params={'value':'42'})
    else:
        # save form title in key within context
        context = {
            "address_form": address_form,
            "building_form": building_form,  # save form in key within context
            "building_title": building_title,
        }
        return render(request, 'building_form.html', context)

def unit_form(request, building_name):
    """
    :param request, building_name:
    :return: unit form page
    """

    unit_title = "Add Unit"
    unit_form = UnitForm()

    # form submitted
    if request.method == 'POST':
        form = UnitForm(request.POST)

        # form valid
        if form.is_valid():
            unit = form.save(commit=False)
            building = Building.objects.get(building_name=building_name)
            building.number_of_units += 1
            unit.building_id = building
            unit.save()  # save input into database

            # Create bedroom
            bedroom = create_room(request, unit, room_type='bedroom')
            create_bedroom_items(request, bedroom)

            # Create kitchen
            kitchen = create_room(request, unit, room_type='kitchen')
            create_kitchen_items(request, kitchen)

            # Create bathroom
            bathroom = create_room(request, unit, room_type='bathroom')
            create_bathroom_items(request, bathroom)

        else:
            return HttpResponse("Invalid login info")
        return HttpResponseRedirect("/buildings/" + building_name + "/")
    else:
        context = {
            "unit_form": unit_form,  # save form in key within context
            "unit_title": unit_title,  # save form title in key within context
            "building_name": building_name,
        }
        return render(request, 'unit_form.html', context)


def room_form(request, building_name, unit_number):
    """
    :param request, building_name & unit #:
    :return: room form page
    """
    room_title = "Add Room"
    room_form = RoomForm()

    # form submitted
    if request.method == 'POST':
        print('post')
        form = RoomForm(request.POST)

        # form valid
        if form.is_valid():
            room = form.save(commit=False)

            # query get
            room.unit_id = Unit.objects.get(building_id__building_name=building_name,
                                            unit_number=unit_number)

            # adds items to rooms
            populate_room(request, form, unit_number)

            room.save()  # save input into database

        else:
            return HttpResponse("Invalid login info")


        # return to previous page
        return HttpResponseRedirect("/buildings/" + building_name + "/" + unit_number + "/")
    else:
        print('no post')
        context = {
            "room_form": room_form,  # save form in key within context
            "room_title": room_title,  # save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
        }
        return render(request, 'room_form.html', context)


def item_form(request, building_name, unit_number, room_name):
    """
    :param request, building_name, unit #, room name:
    :return item form page:
    """

    item_title = "Add Item"
    item_form = ItemForm()  # use fields in ItemForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.room_id = Room.objects.get(unit_id__building_id__building_name=building_name,
                                            unit_id__unit_number=unit_number,
                                            room_name=room_name)
            item.save()  # save input into database
        else:
            return HttpResponse("Invalid login info")

        return HttpResponseRedirect("/buildings/" + building_name + "/" + unit_number + "/" + room_name + "/")
    else:
        context = {
            "item_form": item_form,  # save form in key within context
            "item_title": item_title,  # save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name
        }
        return render(request, 'item_form.html', context)


def item_details_form(request, building_name, unit_number, room_name, item_description):
    """
    :param request, building_name, unit #, room name, item description:
    :return item details form page:
    """

    item_details_title = "Update Item Details"
    item_details_form = ItemDetailsForm()  # use fields in ItemDetailsForm from forms.py
    # vendor_form = VendorForm()

    # if page is submitted
    if request.method == 'POST':
        item_details_form = ItemDetailsForm(request.POST)
        # vendor_form = VendorForm(request.POST)

        # TODO why are my forms not valid?
        if item_details_form.is_valid():
            item_details = item_details_form.save(commit=False)

            # query get
            item_details.item_id = Item.objects.get(room_id__room_name=room_name,
                                                    room_id__unit_id__building_id__building_name=building_name,
                                                    room_id__unit_id__unit_number=unit_number,
                                                    item_description=item_description)
            item_details.save()  # save input into database

        else:
            return HttpResponse("Invalid login info.")

        return HttpResponseRedirect("/buildings/" + building_name + "/" + unit_number + "/" + room_name + "/" + item_description + "/")
    else:
        context = {
            "item_details_form": item_details_form,  # save form in key within context
            "item_details_title": item_details_title,  # save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name,
            "item_description": item_description
        }
        return render(request, 'item_details_form.html', context)

"""---------------------------------------------------------------------------
                             Create Objects
---------------------------------------------------------------------------"""


def create_room(request, unit, room_type):
    """
    :param request, unit, room_type:
    :return room:
    """
    room = Room()
    room.unit_id = unit
    room.room_name = "{}".format(room_type)
    room.save()
    return room

def create_bedroom_items(request, bedroom):
    """
    :param request, bedroom:
    :return bedroom items:
    """
    create_item(request, bedroom, "window pane")
    create_item(request, bedroom, "window sill")
    create_item(request, bedroom, "floor")
    create_item(request, bedroom, "trim")
    create_item(request, bedroom, "walls")
    create_item(request, bedroom, "ceiling light")
    create_item(request, bedroom, "blinds")
    create_item(request, bedroom, "closet")
    create_item(request, bedroom, "closet doors")


def create_kitchen_items(request, kitchen):
    """
    :param request, kitchen:
    :return kitchen items:
    """
    create_item(request, kitchen, "refrigerator")
    create_item(request, kitchen, "sink")
    create_item(request, kitchen, "faucet")
    create_item(request, kitchen, "counters")
    create_item(request, kitchen, "counter lights")
    create_item(request, kitchen, "vinyl")
    create_item(request, kitchen, "top cabinets")
    create_item(request, kitchen, "bottom cabinets")
    create_item(request, kitchen, "blinds")
    create_item(request, kitchen, "walls")
    create_item(request, kitchen, "oven")
    create_item(request, kitchen, "oven lights")
    create_item(request, kitchen, "dish washer")
    create_item(request, kitchen, "window pane")
    create_item(request, kitchen, "window sill")
    create_item(request, kitchen, "ceiling light")
    create_item(request, kitchen, "floor")


def create_bathroom_items(request, bathroom):
    """
    :param request, bathroom:
    :return bathroom items:
    """
    create_item(request, bathroom, "toilet")
    create_item(request, bathroom, "sink")
    create_item(request, bathroom, "faucet")
    create_item(request, bathroom, "bathtub")
    create_item(request, bathroom, "shower")
    create_item(request, bathroom, "vinyl")
    create_item(request, bathroom, "walls")
    create_item(request, bathroom, "ceiling light")
    create_item(request, bathroom, "ceiling fan")
    create_item(request, bathroom, "shower head")
    create_item(request, bathroom, "cabinets")
    create_item(request, bathroom, "counters")
    create_item(request, bathroom, "vanity mirror")
    create_item(request, bathroom, "floor")


def create_item(request, room, item_desc):
    """
    :param request, room, & item_desc:
    :return item:
    """

    # Set attributes for item object
    item = Item()
    item.room_id = room
    item.item_description = "{}".format(item_desc)
    item.save()

    # Create item details
    create_item_details(request, item)

def create_item_details(request, item):
    """
    :param request, item:
    :return item details:
    """
    # vendor = Vendor()
    item_detail = Item_Detail()
    item_detail.item_id = item
    # item_detail.vendor_info = vendor.vendor_name
    item_detail.date = item_detail.item_id.room_id.unit_id.building_id.build_date
    item_detail.cost = 0
    item_detail.vendor = "original"
    # item_detail.install_duration = 0
    item_detail.save()

def populate_room(request, room, unit):
    """
    :param request, room, unit:
    :return room type conditional:
    """

    if room == 'bedroom':
        # Create bedroom
        bedroom = create_room(request, unit, room_type='bedroom')
        create_bedroom_items(request, bedroom)

    elif room == 'kitchen':
        # Create kitchen
        kitchen = create_room(request, unit, room_type='kitchen')
        create_kitchen_items(request, kitchen)

    elif room == 'bathroom':
        # Create bathroom
        bathroom = create_room(request, unit, room_type='bathroom')
        create_bathroom_items(request, bathroom)

"""---------------------------------------------------------------------------
                                Deletions
---------------------------------------------------------------------------"""

# TODO add deletion funtionality?
def delete_building(request, building_name):
    Building.objects.filter(building_name=building_name).delete()
