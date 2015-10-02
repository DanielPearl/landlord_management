from django.shortcuts import render
from .models import *
from .forms import BuildingForm


# Create your views here.

def buildings(request):
    if request.user.is_authenticated():
        title = "Buildings"
        name = "Manager" #models.Manager.user.first_name

    context = {
        "template_title": title,
        "template_name": name,
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
