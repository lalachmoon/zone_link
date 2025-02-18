from django.shortcuts import render
from viewer.models import CourierStreetRange, Zone, ZoneAllocation
from .models import Courier, Polygon
import json
import googlemaps
# from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

gmaps = googlemaps.Client(key="AIzaSyCA0UQ1EUBIqivg6OxBC-vjJZswbpbU1y0")


def home(request):
    return render(request, 'home.html')


def search_courier(request):
    query = request.GET.get('query', '').strip()
    result = None

    if query:
        try:
            street_name, number = query.rsplit(' ', 1)
            number = int(number)
            result = CourierStreetRange.objects.filter(
                street__name__icontains=street_name,
                start_number__lte=number,
                end_number__gte=number
            ).select_related('courier', 'street')

            result = [
                r for r in result
                if r.number_type == 'all' or
                   (r.number_type == 'even' and number % 2 == 0) or
                   (r.number_type == 'odd' and number % 2 != 0)
            ]
        except ValueError:
            result = None

    return render(request, 'search_courier.html', {'result': result, 'query': query})


def map(request):
    couriers = Courier.objects.all()
    polygons = Polygon.objects.all()
    return render(request, 'map.html', {'couriers': couriers, 'polygons': polygons})


# def map(request):
#     polygons = Polygon.objects.filter(user=request.user)
#     polygon_data = [{"coordinates": polygon.coordinates} for polygon in polygons]
#     return render(request, 'map.html',
#                   {'google_maps_api_key': 'AIzaSyCA0UQ1EUBIqivg6OxBC-vjJZswbpbU1y0', 'polygon_data': polygon_data})


def save_polygons(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        polygon_data = data.get('polygonData')

        # Use a default courier or customize as needed
        courier_name = "Default Courier"
        courier, created = Courier.objects.get_or_create(name=courier_name)

        # Create the new polygon with the name and coordinates provided
        zone = Zone.objects.create(
            name=polygon_data['name'],
            coordinates= polygon_data['coordinates']
        )

        zone_allocation = ZoneAllocation.objects.create(
            zone=zone,
            courier=courier,
        )
        return JsonResponse({'message': 'Polygon saved successfully!'})


def edit_polygon(request, polygon_id):
    if request.method == 'POST':
        polygon = get_object_or_404(Polygon, id=polygon_id)
        data = json.loads(request.body)
        polygon.coordinates = data['coordinates']  # Update polygon coordinates
        polygon.save()
        return JsonResponse({'message': 'Polygon updated successfully!'})


def delete_polygon(request, polygon_id):
    if request.method == 'POST':
        polygon = get_object_or_404(Polygon, id=polygon_id)
        polygon.delete()  # Delete the polygon from the database
        return JsonResponse({'message': 'Polygon deleted successfully!'})


def get_polygons(request):
    # Fetch all polygons and return them in JSON format for the frontend
    polygons = Zone.objects.all()
    polygons_data = [
        {"id": polygon.id, "name": polygon.name} for polygon in polygons
    ]
    return JsonResponse({'polygons': polygons_data})

def get_polygon(request, polygon_name):
    polygon = Zone.objects.get(name=polygon_name)
    return JsonResponse({'polygon': {"id": polygon.id, "name": polygon.name, "coordinates": polygon.coordinates}})