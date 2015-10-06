from django.shortcuts import render
from .models import *
from .forms import BuildingForm, UnitForm
from django.http import HttpResponseRedirect


def buildings(request): #building page
    if request.user.is_authenticated():
        title = "Buildings"

        # sets name equal to name attribute in user model
        name = request.user.first_name + " " + request.user.last_name

        # sets building_icons to everything saved in building object
        building_icons = Building.objects.all()

    context = { # Dictionary used by template
        "template_title": title,
        "template_name": name,
        "template_buildings": building_icons,
    }
    return render(request, 'buildings.html', context)

def units(request, building_name): #unit page
    if request.user.is_authenticated():

        # sets name equal to name attribute in building model
        title = building_name

        # sets list to everything saved in unit object
        units = Unit.objects.filter(building_id__building_name=building_name)

        print(units)
        context = { # Dictionary used by template
            "template_units": units,
            "template_building": title,

        }
    return render(request, 'units.html', context)

def building_form(request): #building form page
    title = "Add Building"
    form = BuildingForm()

    if request.method == 'POST': #if page is submitted
        form = BuildingForm(request.POST)
        if form.is_valid(): #if input is valid
            print("here")
            form.save() #save input into database

        else:
            print("else")
        return HttpResponseRedirect("/buildings/") #return to building page
    else:
        context = {
            "form": form, #save form in key within context
            "form_title": title #save form title in key within context
        }
        return render(request, 'building_form.html', context)

def unit_form(request, building_name): #building form page
    title = "Add Unit"
    form = UnitForm()

    if request.method == 'POST': #if page is submitted
        form = UnitForm(request.POST)
        if form.is_valid(): #if input is valid
            print("here")
            form.save() #save input into database
        else:
            print("else")

        units = Unit.objects.filter(building_id__building_name=building_name)
        return HttpResponseRedirect("/units/") #return to building page
    else:
        context = {
            "form": form, #save form in key within context
            "form_title": title #save form title in key within context
        }
        return render(request, 'unit_form.html', context)
