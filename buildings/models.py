from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.street_number) + " " + self.street_name + ", #" + \
            self.unit_number + ", " + self.city + ", " + self.state + " " + \
               str(self.zip_code)

class Manager(models.Model):
    user = models.OneToOneField(User)
    start_date = models.DateField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    manager_id = models.ManyToManyField(Manager)
    address_id = models.ForeignKey(Address)
    building_name = models.CharField(max_length=30)
    build_date = models.DateField(blank=True)
    number_of_units = models.IntegerField(default=None)

    def __str__(self):
        return self.building_name

class Unit(models.Model):
    building_id = models.ForeignKey(Building)
    unit_number = models.CharField(max_length=30)
    parking_space = models.CharField(max_length=30)
    is_rented = models.BooleanField(default=False)

    def __str__(self):
        return "unit #" + self.unit_number

class Tenant(models.Model):
    unit_id = models.ForeignKey(Unit)
    tenant_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images', height_field=None,
                              width_field=None, max_length=100,
                              default=None)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    move_in = models.DateField()

    def __str__(self):
        return self.tenant_name

class Room(models.Model):
    unit_id = models.ForeignKey(Unit)
    room_name = models.CharField(max_length=30)

    def __str__(self):
        return self.room_name

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    address_id = models.OneToOneField(Address)
    email = models.EmailField(max_length=30)
    website = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)

    def __str__(self):
        return self.vendor_name

class Item(models.Model):
    room_id = models.ForeignKey(Room)
    item_description = models.CharField(max_length=30)

    def __str__(self):
        return self.item_description

class Item_Detail(models.Model):
    item_id = models.ManyToManyField(Item)
    vendor_info = models.ForeignKey(Vendor)
    date = models.DateField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    # install_duration = models.FloatField()

    def __str__(self):
        return self.item_id