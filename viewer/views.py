from django.shortcuts import render
from viewer.models import CourierStreetRange
from .models import Courier
import json
import googlemaps
# from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .models import Polygon

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
    return render(request, 'map.html')

# def map(request):
#     polygons = Polygon.objects.filter(user=request.user)
#     polygon_data = [{"coordinates": polygon.coordinates} for polygon in polygons]
#     return render(request, 'map.html',
#                   {'google_maps_api_key': 'AIzaSyCA0UQ1EUBIqivg6OxBC-vjJZswbpbU1y0', 'polygon_data': polygon_data})


def save_polygons(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        for courier_data in data:
            courier_name = courier_data.get('name')
            courier, created = Courier.objects.get_or_create(name=courier_name)

            for polygon_data in courier_data.get('polygonData', []):
                Polygon.objects.create(
                    courier=courier,
                    name=f"{courier_name} Polygon",
                    coordinates=polygon_data
                )

        return JsonResponse({'message': 'Polygons saved successfully!'})
