from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, TextField, CASCADE, SET_NULL, \
    PositiveIntegerField
from django.db import models


# Country model
class Country(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


# County model
class County(Model):
    country = ForeignKey(Country, on_delete=CASCADE)
    name = CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.country.name}'


# City model
class City(Model):
    county = ForeignKey(County, on_delete=CASCADE)
    name = CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.county.name}'


# Neighborhood model
class Neighborhood(Model):
    city = ForeignKey(City, on_delete=CASCADE)
    name = CharField(max_length=100)

    def __str__(self):
        return f'{self.name}, {self.city.name}'


# Zone model
class Zone(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


# Street model
class Street(Model):
    neighborhood = ForeignKey(Neighborhood, on_delete=CASCADE)
    name = CharField(max_length=100)
    zone = ForeignKey(Zone, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.neighborhood.name}'


# Courier model
class Courier(Model):
    name = CharField(max_length=100)
    zone = ForeignKey(Zone, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


# CourierStreetRange
class CourierStreetRange(Model):
    NUMBER_TYPE_CHOICES = [
        ('all', 'All Numbers'),
        ('even', 'Even Numbers'),
        ('odd', 'Odd Numbers'),
    ]

    courier = ForeignKey(Courier, on_delete=CASCADE)
    street = ForeignKey(Street, on_delete=CASCADE)
    start_number = PositiveIntegerField()
    end_number = PositiveIntegerField()
    number_type = CharField(
        max_length=10,
        choices=NUMBER_TYPE_CHOICES,
        default='all',
        help_text='Specify if the courier serves all numbers, only even numbers or only odd numbers'
    )

class PolygonModel(models.Model):
    name = models.CharField(max_length=100)  # Name of the polygon (e.g., "Polygon 1")
    coordinates = models.JSONField()  # To store polygon coordinates as a dictionary
    def __str__(self):
        return f'{self.courier.name}, ({self.start_number}-{self.end_number})'

