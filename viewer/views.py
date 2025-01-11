from django.shortcuts import render
from viewer.models import CourierStreetRange


def home(request):
    return render(request, 'home.html')


def subscriptions(request):
    return render(request, 'subscriptions.html')


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
