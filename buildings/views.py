from django.shortcuts import render
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

"""---------------------------------------------------------------------------
                                Authentication
---------------------------------------------------------------------------"""
def login_user(request):
    """Login user form"""

    logout_user(request)
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # user authentication for username & password
        user = authenticate(username=username, password=password)

        #If user is registered
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/buildings/')
        #if user is not registered
        else:
            return HttpResponse("Invalid login info")
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/buildings/')
        #if not authenticated stay on homepage
        else:
            return render(request, 'homepage.html')

def register_form(request):
    """Register user form"""

    register_title = "Register"
    registered = False

    #if form is submitted, save user and manager info
    if request.method == 'POST':
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user_form = UserForm(data = request.POST)
        manager_form = ManagerForm(data = request.POST)

        #if user and manager fields are valid
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

        #If user is registered
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect("/buildings/") #return to building page
        #if user and manager fields are not valid
        else:
            print(user_form.errors, manager_form.errors)
    #if form has not been submitted
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
    """Logout user"""

    logout(request)
    return HttpResponseRedirect('/')


"""---------------------------------------------------------------------------
                                Page Renders
---------------------------------------------------------------------------"""
def buildings(request):
    """Render buildings page"""

    if request.user.is_authenticated():
        title = "Buildings"

        # sets building_icons to everything saved in building object
        buildings = Building.objects.filter(manager_id__user=request.user)
        # sets name equal to name attribute in user model
        name = request.user.first_name + " " + request.user.last_name

        # Dictionary keys to be used in templates
        context = {
            "title": title,
            "manager_name": name,
            "buildings": buildings
        }
        return render(request, 'buildings.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

def units(request, building_name):
    """Render units page"""

    if request.user.is_authenticated():

        # populates page with units saved in the database
        units = Unit.objects.filter(building_id__manager_id__user=request.user, building_id__building_name=building_name)

        # Dictionary keys to be used in templates
        context = {
            "units": units.sort(),
            "building_name": building_name,
        }
        return render(request, 'units.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

def rooms(request, building_name, unit_number):
    """Render rooms page"""

    if request.user.is_authenticated():

        # sets name equal to name attribute in room model
        title = building_name + ", #" + unit_number

        # sets list to everything saved in room object
        rooms = Room.objects.filter(unit_id__building_id__manager_id__user=request.user,
            unit_id__unit_number=unit_number, unit_id__building_id__building_name=building_name)

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
    """Item details page"""

    if request.user.is_authenticated():

        # sets name equal to name attribute in item model
        title = building_name + ", #" + unit_number + ", " + room_name

        # sets list to everything saved in item object
        items = Item.objects.filter(room_id__unit_id__building_id__manager_id__user=request.user,
            room_id__room_name=room_name,room_id__unit_id__unit_number=unit_number, room_id__unit_id__building_id__building_name=building_name)

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
    """Render item details page"""

    if request.user.is_authenticated():

        # sets name equal to name attribute in item detail model
        title = building_name + ", #" + unit_number + ", " + room_name + ", " + item_description

        # sets list to everything saved in item detail object
        item_details = Item_Detail.objects.filter(item_id__room_id__unit_id__building_id__manager_id__user=request.user, item_id__item_description=item_description,
            item_id__room_id__room_name=room_name,item_id__room_id__unit_id__unit_number=unit_number,item_id__room_id__unit_id__building_id__building_name=building_name)

        context = { # Dictionary used by template
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
    """Create building form"""

    building_title = "Add Building"
    building_form = BuildingForm() #use fields in BuildingForm from forms.py
    address_form = AddressForm()

    #if form is submitted, save building and address info
    if request.method == 'POST':
        building_form = BuildingForm(request.POST)
        address_form = AddressForm(request.POST)

        #if input is valid, save form into database
        if building_form.is_valid() and address_form.is_valid():
            #building_form.save()
            address = address_form.save()

            building = building_form.save(commit=False)
            building.address_id = address
            building.save()

            # If no buildings exist in the database
            if building.number_of_units > 0:
                for i in range(building.number_of_units):
                    # Create unit
                    unit = Unit()
                    unit.unit_number = i+1
                    unit.building_id = building
                    unit.is_rented = False
                    unit.parking_space = "no parking"
                    unit.save()

                    # Create bedroom
                    bedroom = Room()
                    bedroom.unit_id = unit
                    bedroom.room_name = "bedroom"
                    bedroom.save()

                    # Create kitchen
                    kitchen = Room()
                    kitchen.unit_id = unit
                    kitchen.room_name = "kitchen"
                    kitchen.save()

                    # Create bathroom
                    bathroom = Room()
                    bathroom.unit_id = unit
                    bathroom.room_name = "bathroom"
                    bathroom.save()

                    # Create items
                    bedroom_items = create_bedroom_items(request, bedroom)
                    kitchen_items = create_kitchen_items(request, kitchen)
                    bathroom_items = create_bathroom_items(request, bathroom)

            username = Manager.objects.get(user=request.user)
            building.manager_id.add(username)
            building.save() #save input into database

            return HttpResponseRedirect("/buildings/") #return to building page
        else:
            return HttpResponse("Invalid login info")
            # raise forms.ValidationError("Please enter something")
            # raise ValidationError(_('Invalid value%(value)s'),code="invalid",params={'value':'42'})
    else:
        #save form title in key within context
        context = {
            "address_form": address_form,
            "building_form": building_form, #save form in key within context
            "building_title": building_title,
        }
        return render(request, 'building_form.html', context)

def create_bedroom(request, unit):
    pass

def create_bedroom_items(request, bedroom):
    """Create items found in bedroom"""

    item = "window pane"
    create_item(request, bedroom, item)
    item = "window sill"
    create_item(request, bedroom, item)
    item = "floor"
    create_item(request, bedroom, item)
    item = "trim"
    create_item(request, bedroom, item)
    item = "walls"
    create_item(request, bedroom, item)
    item = "ceiling light"
    create_item(request, bedroom, item)
    item = "blinds"
    create_item(request, bedroom, item)
    item = "closet"
    create_item(request, bedroom, item)
    item = "closet doors"
    create_item(request, bedroom, item)

def create_kitchen_items(request, kitchen):
    """Create items found in kitchen"""

    item = "refrigerator"
    create_item(request, kitchen, item)
    item = "sink"
    create_item(request, kitchen, item)
    item = "faucet"
    create_item(request, kitchen, item)
    item = "counters"
    create_item(request, kitchen, item)
    item = "counter lights"
    create_item(request, kitchen, item)
    item = "vinyl"
    create_item(request, kitchen, item)
    item = "top cabinets"
    create_item(request, kitchen, item)
    item = "bottom cabinets"
    create_item(request, kitchen, item)
    item = "blinds"
    create_item(request, kitchen, item)
    item = "walls"
    create_item(request, kitchen, item)
    item = "oven"
    create_item(request, kitchen, item)
    item = "oven lights"
    create_item(request, kitchen, item)
    item = "dish washer"
    create_item(request, kitchen, item)
    item = "window pane"
    create_item(request, kitchen, item)
    item = "window sill"
    create_item(request, kitchen, item)
    item = "ceiling light"
    create_item(request, kitchen, item)
    item = "floor"
    create_item(request, kitchen, item)

def create_bathroom_items(request, bathroom):
    """Create items found in bathroom"""

    item = "toilet"
    create_item(request, bathroom, item)
    item = "sink"
    create_item(request, bathroom, item)
    item = "faucet"
    create_item(request, bathroom, item)
    item = "bathtub"
    create_item(request, bathroom, item)
    item = "shower"
    create_item(request, bathroom, item)
    item = "vinyl"
    create_item(request, bathroom, item)
    item = "walls"
    create_item(request, bathroom, item)
    item = "ceiling light"
    create_item(request, bathroom, item)
    item = "ceiling fan"
    create_item(request, bathroom, item)
    item = "shower head"
    create_item(request, bathroom, item)
    item = "cabinets"
    create_item(request, bathroom, item)
    item = "counters"
    create_item(request, bathroom, item)
    item = "vanity mirror"
    create_item(request, bathroom, item)
    item = "floor"
    create_item(request, bathroom, item)

def create_item(request, room, new_item):
    """Create items in all rooms"""

    # Set attributes for item object
    item = Item()
    item.room_id = room
    item.item_description = "{}".format(new_item)

    item.save()

    # create_item_details(request, new_item)

    
    # Create item details

def create_item_details(request, new_item):
    """Create item details for items"""

    item_detail = Item_Detail()
    item_detail.item_id = new_item
    item_detail.vendor_info = "original"
    item_detail.date = item_detail.item_id.room_id.unit_id.building_id.build_date
    item_detail.cost = 0
    item_detail.install_duration = 0
    item_detail.save()

def unit_form(request, building_name):
    """Create unit form"""

    unit_title = "Add Unit"
    unit_form = UnitForm() #use fields in UnitForm fs.py
    #if page is submitted
    if request.method == 'POST':
        form = UnitForm(request.POST)
        #if input is valid
        if form.is_valid():
            unit = form.save(commit=False)
            unit.building_id = Building.objects.get(building_name=building_name)
            unit.save() #save input into database

            # Create bedroom
            bedroom = Room()
            bedroom.unit_id = unit
            bedroom.room_name = "bedroom"
            bedroom.save()

            # Create kitchen
            kitchen = Room()
            kitchen.unit_id = unit
            kitchen.room_name = "kitchen"
            kitchen.save()

            # Create bathroom
            bathroom = Room()
            bathroom.unit_id = unit
            bathroom.room_name = "bathroom"
            bathroom.save()

            # Create items
            bedroom_items = create_bedroom_items(request, bedroom)
            kitchen_items = create_kitchen_items(request, kitchen)
            bathroom_items = create_bathroom_items(request, bathroom)

        else:
            return HttpResponse("Invalid login info")
        #return to previous page
        return HttpResponseRedirect("/buildings/units/" + building_name)
    else:
        context = {
            "unit_form": unit_form, #save form in key within context
            "unit_title": unit_title, #save form title in key within context
            "building_name": building_name,
        }
        return render(request, 'unit_form.html', context)

def room_form(request, building_name, unit_number):
    """Create room form"""

    room_title = "Add Room"
    room_form = RoomForm() #use fields in RoomForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        print('post')
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.unit_id = Unit.objects.get(building_id__building_name=building_name, unit_number=unit_number)
            room.save() #save input into database

        else:
            return HttpResponse("Invalid login info")


        #return to previous page
        return HttpResponseRedirect("/buildings/units/rooms/" + building_name + "/" + unit_number)
    else:
        print('no post')
        context = {
            "room_form": room_form, #save form in key within context
            "room_title": room_title, #save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
        }
        return render(request, 'room_form.html', context)

def item_form(request, building_name, unit_number, room_name):
    """Create item form"""

    item_title = "Add Item"
    item_form = ItemForm() # use fields in ItemForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        form = ItemForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.room_id = Room.objects.get(unit_id__building_id__building_name=building_name, unit_id__unit_number=unit_number, room_name=room_name)
            post.save() # save input into database
        else:
            return HttpResponse("Invalid login info")

        return HttpResponseRedirect("/buildings/units/rooms/items/" + building_name + "/" + unit_number + "/" + room_name)
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
    """Create item detail from"""

    item_details_title = "Add Item Details"
    item_details_form = ItemDetailsForm()  # use fields in ItemDetailsForm from forms.py
    vendor_form = VendorForm()

    # if page is submitted
    if request.method == 'POST':
        item_details_form = ItemDetailsForm(request.POST)
        vendor_form = VendorForm(request.POST)

        if item_details_form.is_valid() and vendor_form.is_valid():

            item_details_form.save()
            vendor = vendor_form.save()

            item_details = item_details_form.save(commit=False)
            item_details.vendor_id = vendor
            item_details.item_id = Item.objects.get(room_id__room_name=room_name, room_id__unit_id__building_id__building_name=building_name,
                                            room_id__unit_id__unit_number=unit_number, item_description=item_description)
            item_details.save()  # save input into database

        else:
            return HttpResponse("Invalid login info")

        # return to previous page
        return HttpResponseRedirect("/buildings/units/rooms/items/item_details/" + building_name + "/" + unit_number + "/" + room_name + "/" + item_description)
    else:
        context = {
            "item_details_form": item_details_form,  # save form in key within context
            "vendor_form": vendor_form,
            "item_details_title": item_details_title,  # save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name,
            "item_description": item_description
        }
        return render(request, 'item_details_form.html', context)

# def delete(request):

"""---------------------------------------------------------------------------
                                Deletions
---------------------------------------------------------------------------"""

def delete_building(request, building_name):
    Building.objects.filter(building_name=building_name).delete()
