from django.shortcuts import render
from viewer.models import CourierStreetRange
from django.http import HttpResponse
import requests
import googlemaps
# from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PolygonModel
from .forms import PolygonForm

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


# def zone_mapping(request):
#     pass


def zone_mapping(request):
    if request.method == "POST":
        # Replace with your Google API key
        GOOGLE_MAPS_API_KEY = "AIzaSyCA0UQ1EUBIqivg6OxBC-vjJZswbpbU1y0"

        # Get the location data from the form
        location = request.POST.get("location")
        zoom = request.POST.get("zoom", 12)

        # Generate the Static Map API URL
        map_url = f"https://www.google.com/maps/search/?api=1&query=45.68453939481016%2C25.598650239556875={location}&zoom={zoom}&size=600x400&key={GOOGLE_MAPS_API_KEY}"

    return render(request, "map.html", {"map_url": map_url, "location": location})

# def interactive_map(request):
#     return render(request, "interactive_map.html")


# View to add and list polygons
def manage_polygons(request):
    if request.method == "POST":
        form = PolygonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_polygons')
    else:
        form = PolygonForm()

    # Fetch all polygons to display them on the map
    polygons = PolygonModel.objects.all()
    polygon_data = [
        {
            "name": polygon.name,
            "coordinates": polygon.coordinates
        }
        for polygon in polygons
    ]

    return render(request, "manage_polygons.html", {
        "form": form,
        "polygon_data": polygon_data,
    })

# API to dynamically fetch polygon coordinates
def get_polygons(request):
    polygons = PolygonModel.objects.all()
    polygon_data = [
        {
            "name": polygon.name,
            "coordinates": polygon.coordinates
        }
        for polygon in polygons
    ]
    return JsonResponse({"polygons": polygon_data})




