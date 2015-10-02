from django.contrib import admin
from .models import *
from .forms import Building

# Register your models here.
admin.site.register(Address)
admin.site.register(Manager)
admin.site.register(Building)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Room)
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Item_Detail)