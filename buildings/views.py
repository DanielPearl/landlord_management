from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


"""---------------------------------------------------------------------------
                                Authentication
---------------------------------------------------------------------------"""
def login_user(request):
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

#Register Form
def register_form(request):
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
    logout(request)
    return HttpResponseRedirect('/')


"""---------------------------------------------------------------------------
                                Page Renders
---------------------------------------------------------------------------"""
#Building Page
def buildings(request):
    if request.user.is_authenticated():
        title = "Buildings"

        # sets building_icons to everything saved in building object
        buildings = Building.objects.filter(manager_id__user=request.user)

        # sets name equal to name attribute in user model
        name = request.user.first_name + " " + request.user.last_name

        context = { # Dictionary used by template
            "title": title,
            "manager_name": name,
            "buildings": buildings,
        }
        return render(request, 'buildings.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

#Units Page
def units(request, building_name):
    if request.user.is_authenticated():

        # sets list to everything saved in unit object
        units = Unit.objects.filter(building_id__manager_id__user=request.user, building_id__building_name=building_name)
        # building_date = Unit.objects.filter(building_id__build_date=building_name)

        context = { # Dictionary used by template
            "units": units,
            "building_name": building_name,
            # "building_date": building_date
        }
        return render(request, 'units.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

#Rooms Page
def rooms(request, building_name, unit_number):
    if request.user.is_authenticated():

        # sets name equal to name attribute in building model
        title = building_name + ", #" + unit_number

        # sets list to everything saved in unit object
        rooms = Room.objects.filter(unit_id__building_id__manager_id__user=request.user,
            unit_id__unit_number=unit_number, unit_id__building_id__building_name=building_name)

        context = { # Dictionary used by template
            "title": title,
            "rooms": rooms,
            "building_name": building_name,
            "unit_number": unit_number,
        }
        return render(request, 'rooms.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

#Rooms Page
def items(request, building_name, unit_number, room_name):
    if request.user.is_authenticated():

        # sets name equal to name attribute in building model
        title = building_name + ", #" + unit_number + ", " + room_name

        # sets list to everything saved in unit object
        items = Item.objects.filter(room_id__unit_id__building_id__manager_id__user=request.user,
            room_id__room_name=room_name,room_id__unit_id__unit_number=unit_number, room_id__unit_id__building_id__building_name=building_name)

        context = { # Dictionary used by template
            "template_items": items,
            "template_title": title,
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name,
        }
        return render(request, 'items.html', context)
    else:
        logout_user(request)
        return HttpResponseRedirect('/')

"""---------------------------------------------------------------------------
                                Forms
---------------------------------------------------------------------------"""
#Building Form
def building_form(request): #building form page
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

            post = building_form.save(commit=False)
            post.address_id = address
            post.save() #save input into database

            username = Manager.objects.get(user=request.user)
            post.manager_id.add(username)
            post.save() #save input into database

            #return to buildings page
            return HttpResponseRedirect("/buildings/") #return to building page
    else:
        #save form title in key within context
        context = {
            "address_form": address_form,
            "building_form": building_form, #save form in key within context
            "building_title": building_title,
        }
        return render(request, 'building_form.html', context)

#Unit Form
def unit_form(request, building_name): #building form page
    unit_title = "Add Unit"
    unit_form = UnitForm() #use fields in UnitForm fs.py

    #if page is submitted
    if request.method == 'POST':
        form = UnitForm(request.POST)
        #if input is valid
        if form.is_valid():
            post = form.save(commit=False)
            post.building_id = Building.objects.get(building_name=building_name)
            post.save() #save input into database

        #return to previous page
        return HttpResponseRedirect("/buildings/units/" + building_name)
    else:
        context = {
            "unit_form": unit_form, #save form in key within context
            "unit_title": unit_title, #save form title in key within context
            "building_name": building_name,
        }
        return render(request, 'unit_form.html', context)

#Room Form
def room_form(request, building_name, unit_number): #building form page
    room_title = "Add Room"
    room_form = RoomForm() #use fields in UnitForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        print('post')
        form = RoomForm(request.POST)

        #if form.is_valid():
        post = form.save(commit=False)
        post.unit_id = Unit.objects.get(building_id__building_name=building_name, unit_number=unit_number)
        post.save() #save input into database

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

#Item Form
def item_form(request, building_name, unit_number, room_name): #building form page
    item_title = "Add Item"
    item_form = ItemForm() #use fields in UnitForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        form = ItemForm(request.POST)

        #if form.is_valid():
        post = form.save(commit=False)
        post.room_id = Room.objects.get(unit_id__building_id__building_name=building_name, unit_id__unit_number=unit_number, room_name=room_name)
        post.save() #save input into database

        #return to previous page
        return HttpResponseRedirect("/buildings/units/rooms/items/" + building_name + "/" + unit_number + "/" + room_name)
    else:
        context = {
            "item_form": item_form, #save form in key within context
            "item_title": item_title, #save form title in key within context
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name
        }
        return render(request, 'item_form.html', context)


"""---------------------------------------------------------------------------
                                Deletions
---------------------------------------------------------------------------"""

def delete_building(request, building_name):
    Building.objects.filter(building_name=building_name).delete()


