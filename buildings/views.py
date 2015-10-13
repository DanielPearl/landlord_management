from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


"""---------------------------------------------------------------------------
                                Authentication
---------------------------------------------------------------------------"""
def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/buildings/')
            else:
                return HttpResponse("Invalid account")
        else:
            print("Invalid login information")
            return HttpResponse("Invalid login information")
    else:
        return render(request, 'homepage.html')

def Register(request):
    registered = False
    if request.method == 'POST':
        user_form = Login(data=request.POST)
        manager_form = Manager(data=request.POST)

        if user_form.is_valid() and manager_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            manager = manager_form.save(commit=False)
            manager.user = user

            manager.save()
            registered = True

            return HttpResponseRedirect("/buildings/")
        else:
            print(user_form.errors, manager_form.errors)
    else:
        user_form = Login()
        manager_form = Manager()

    return render(request, 'homepage.html', {'user_form':user_form, 'manager_form':manager_form, 'registered': registered})

# def login(request): #building form page
#     title = "Login"
#     form = Login() #use fields in BuildingForm from forms.py
#     username = request.POST['username']
#     password = request.POST['password']
#
#     user = authenticate(username=username, password=password)
#
#     #if page is submitted, save form as BuildingForm
#     if user is not None:
#         if user.is_active:
#             if form.is_valid():
#                 login(request, user)
#                 return HttpResponseRedirect(("/buildings/"))
#         else:
#             context = {
#                 "form": form, #save form in key within context
#                 "form_title": title #save form title in key within context
#             }
#         return render(request, 'homepage.html', context)

def logout(request):
    logout(request)
    return render(request, 'homepage.html')



"""---------------------------------------------------------------------------
                                Page Renders
---------------------------------------------------------------------------"""
#Building Page
def buildings(request):
    if request.user.is_authenticated():
        title = "Buildings"

        # sets name equal to name attribute in user model
        name = request.user.first_name + " " + request.user.last_name

        # sets building_icons to everything saved in building object
        buildings = Building.objects.all()

    context = { # Dictionary used by template
        "title": title,
        "manager_name": name,
        "buildings": buildings,
    }
    return render(request, 'buildings.html', context)

#Units Page
def units(request, building_name):
    if request.user.is_authenticated():

        # sets list to everything saved in unit object
        units = Unit.objects.filter(building_id__building_name=building_name)

        context = { # Dictionary used by template
            "units": units,
            "building_name": building_name,
        }
    return render(request, 'units.html', context)

#Rooms Page
def rooms(request, building_name, unit_number):
    if request.user.is_authenticated():

        # sets name equal to name attribute in building model
        title = building_name + ", #" + unit_number

        # sets list to everything saved in unit object
        rooms = Room.objects.filter(
            unit_id__unit_number=unit_number,unit_id__building_id__building_name=building_name)

        context = { # Dictionary used by template
            "title": title,
            "rooms": rooms,
            "building_name": building_name,
            "unit_number": unit_number,
        }
    return render(request, 'rooms.html', context)

#Rooms Page
def items(request, building_name, unit_number, room_name):
    if request.user.is_authenticated():

        # sets name equal to name attribute in building model
        title = building_name + ", #" + unit_number + ", " + room_name

        # sets list to everything saved in unit object
        items = Item.objects.filter(
            room_id__room_name=room_name,room_id__unit_id__unit_number=unit_number, room_id__unit_id__building_id__building_name=building_name)

        context = { # Dictionary used by template
            "template_items": items,
            "template_title": title,
            "building_name": building_name,
            "unit_number": unit_number,
            "room_name": room_name,
        }
    return render(request, 'items.html', context)

"""---------------------------------------------------------------------------
                                Forms
---------------------------------------------------------------------------"""
#Building Form
def building_form(request): #building form page
    building_title = "Add Building"
    building_form = BuildingForm() #use fields in BuildingForm from forms.py
    address_form = AddressForm()

    #if page is submitted, save form as BuildingForm
    if request.method == 'POST':
        building_form = BuildingForm(request.POST)
        address_form = AddressForm(request.POST)

        #if input is valid, save form into database
        if building_form.is_valid() and address_form.is_valid():
            building_form.save()
            address_form.save()

        #return to previous page
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
    unit_form = UnitForm() #use fields in UnitForm f        s.py
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
            "building_name": building_name
        }
        return render(request, 'unit_form.html', context)

#Room Form
def room_form(request, building_name, unit_number): #building form page
    room_title = "Add Unit"
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
    item_title = "Add Unit"
    item_form = ItemForm() #use fields in UnitForm from forms.py
    #     #if page is submitted

    if request.method == 'POST':
        form = ItemForm(request.POST)

        #if form.is_valid():
        post = form.save(commit=False)
        post.room_id = Room.objects.get(room_name=room_name)
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