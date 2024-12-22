from django.shortcuts import render
# from django.contrib.gis.geos import Point
# from django.contrib.gis.db.models.functions import Distance
from viewer.models import CourierStreetRange, Zone, Courier


# Search for courier by street and number

def search_courier(request):
    query = request.GET.get('query')
    result = None

    if query:
        try:
            street_name, number = query.rsplit(' ', 1)
            number = int(number)

            # Search by street and number
            result = CourierStreetRange.objects.filter(
                street__name__icontains=street_name,
                start_number__lte=number,
                end_number__gte=number
            ).select_related('courier', 'street')

            # Filter based on number_type
            result = [
                r for r in result
                if r.number_type == 'all' or
                (r.number_type == 'even' and number % 2 == 0) or
                (r.number_type == 'odd' and number % 2 != 0)
            ]

            # # Search by zone
            # if not result:
            #     # Replace with real latitude and longitude from Google API
            #     lat, lon = 40.7128, - 74.0060
            #     point = Point(lon, lat)
            #     zone = Zone.objects.annotate(distance=Distance('boundary', point)).order_by('distance').first()
            #     if zone:
            #         result = Courier.objects.filter(zone=zone).first()
            #     else:
            #         result = None

        except ValueError:
            result = None
    return render(request, 'search_courier.html', {'result': result, 'query': query})

print(CourierStreetRange.objects.all())
