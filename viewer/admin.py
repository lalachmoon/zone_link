from django.contrib import admin
from .models import Country, County, City, Neighborhood, Street, Courier, CourierStreetRange, Zone


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county']


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name', 'neighborhood', 'zone']


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['name', 'zone']


@admin.register(CourierStreetRange)
class CourierStreetRangeAdmin(admin.ModelAdmin):
    list_display = ['courier', 'street', 'start_number', 'end_number', 'number_type']
    list_filter = ['number_type']


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']



