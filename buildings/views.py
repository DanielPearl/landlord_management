from django.shortcuts import render
from .models import *
from .forms import BuildingForm


def buildings(request):
    if request.user.is_authenticated():
        title = "Buildings"
        name = request.user.first_name + " " + request.user.last_name

        building_icons = Building.objects.all()

    context = {
        "template_title": title,
        "template_name": name,
        "template_buildings": building_icons,
    }
    return render(request, 'buildings.html', context)

def building_form(request):

    #title = "Add Building"
    form = BuildingForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        #"form_title": title
    }
    return render(request, 'building_form.html',context)
