from django.shortcuts import render
from viewer.models import CourierStreetRange


def home(request):
    return render(request, 'home.html')


def subscriptions(request):
    plans = [
        {
            'name': 'Basic',
            'description': 'Full access',
            'price': '$120/month',
            'slug': 'basic',
        },
        {
            'name': 'Professional',
            'description': 'Full access',
            'price': '$560/half year',
            'slug': 'professional',
        },
        {
            'name': 'Enterprise',
            'description': 'Full access',
            'price': '$1000/month',
            'slug': 'enterprise',
        },

    ]

    return render(request, 'subscriptions.html', {'plans': plans})


def subscribe(request, plan_slug):
    plans = {
        'basic': {'name': 'Basic', 'price': '$120/month'},
        'professional': {'name': 'Professional', 'price': '$560/half year'},
        'enterprise': {'name': 'Enterprise', 'price': '$1000/year'},
    }
    selected_plan = plans.get(plan_slug, None)
    if not selected_plan:
        return render(request, '404.html')

    # Pass individual plan fields
    return render(request, 'subscribe.html', {
        'plan_name': selected_plan['name'],
        'plan_price': selected_plan['price']
    })


def search_courier(request):
    query = request.GET.get('query', '').strip()
    result = None

    if query:
        try:
            # Normalize the input
            '''
               Convert input to lowercase: query.lower()
               Remove commas and "nr" (common delimiters): .replace(',', '').replace('nr', '')
               Strip extra spaces: .strip()
            '''
            query = query.lower().replace(',', '').replace('nr', '').strip()
            parts = query.split()
            ''' 
                Split the normalized input into parts: query.split()
                Assume the last part is the number: parts[-1]
                Rejoin the rest as the street name: ' '.join(parts[:-1])
            '''
            # Extract the number (last part of the input) and rejoin the rest as the street name
            number = int(parts[-1])  # Last part is the number
            street_name = ' '.join(parts[:-1]).title()  # Remaining parts form the street name

            # Filter based on street and number range
            result = CourierStreetRange.objects.filter(
                street__name__icontains=street_name,
                start_number__lte=number,
                end_number__gte=number
            ).select_related('courier', 'street')

            # Filter for odd/even/all number types
            result = [
                r for r in result
                if r.number_type == 'all' or
                (r.number_type == 'even' and number % 2 == 0) or
                (r.number_type == 'odd' and number % 2 != 0)
            ]
        except (ValueError, IndexError):
            result = None

    return render(request, 'search_courier.html', {'result': result, 'query': query})
