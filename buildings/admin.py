from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Login)
admin.site.register(Address)
admin.site.register(Manager)
admin.site.register(Building)
admin.site.register(Tenant)
admin.site.register(Unit)
admin.site.register(Room)
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Item_Detail)