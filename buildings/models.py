from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class Address(models.Model):
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=30)
    unit_number = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()

class Manager(models.Model):
    username = models.CharField(max_length=30)
    address_id = models.OneToOneField(Address)
    manager_name = models.CharField(max_length=30)
    start_date = models.DateField()
    phone_number = models.IntegerField()
    email = models.CharField(max_length=30)

class Building(models.Model):
    manager_id = models.ForeignKey(Manager)
    address_id = models.OneToOneField(Address)
    building_name = models.CharField(max_length=30)
    occupancy = models.IntegerField()
    build_date = models.DateField()

class Unit(models.Model):
    building_id = models.ForeignKey(Building)
    unit_number = models.CharField(max_length=30)
    parking_space = models.CharField(max_length=30)

class Tenant(models.Model):
    unit_id = models.ForeignKey(Unit)
    tenant_names = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    move_in = models.DateField()

class Room(models.Model):
    unit_id = models.ForeignKey(Unit)
    name = models.CharField(max_length=30)

class Vendor(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    address_id = models.OneToOneField(Address)
    email = models.EmailField(max_length=30)
    website = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)

class Item(models.Model):
    room_id = models.ForeignKey(Room)
    item_description = models.CharField(max_length=30)

class Item_Detail(models.Model):
    item_id = models.ManyToManyField(Item)
    vendor_info = models.ForeignKey(Vendor)
    date = models.DateField()
    cost = models.FloatField()
    install_duration = models.IntegerField()

