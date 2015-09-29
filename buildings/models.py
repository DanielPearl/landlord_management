from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

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

    def __str__(self):
        return self.manager_name

class Building(models.Model):
    manager_id = models.ManyToManyField(Manager)
    address_id = models.ForeignKey(Address)
    building_name = models.CharField(max_length=30)
    occupancy = models.IntegerField()
    build_date = models.DateField()

    def __str__(self):
        return self.building_name

class Unit(models.Model):
    building_id = models.ForeignKey(Building)
    unit_number = models.CharField(max_length=30)
    parking_space = models.CharField(max_length=30)

    def __str__(self):
        return self.unit_number

class Tenant(models.Model):
    unit_id = models.ForeignKey(Unit)
    tenant_name = models.CharField(max_length=100)
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
    cost = models.FloatField()
    install_duration = models.IntegerField()

