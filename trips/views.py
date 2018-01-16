from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.http import JsonResponse

from .models import Trip, Location
from .forms import NewTripForm


@login_required
def dashboard(request):
    num_planned_trips = Trip.objects.filter(creator=request.user).count()
    num_joined_trips = Trip.objects.filter(followers=request.user).count()

    data = {'num_planned_trips': num_planned_trips, 'num_joined_trips': num_joined_trips, }
    return render(request, 'trips/dashboard.html', data)


@login_required
def add_new_trip(request):
    if request.method == 'POST':
        form = NewTripForm(request.POST)
        if form.is_valid():
            trip = Trip(creator=request.user, start_date=form.cleaned_data['start_date'],
                        finish_date=form.cleaned_data['finish_date'])
            trip.save()

            origin_location = Location(name=form.cleaned_data['origin_input'])
            origin_location.lat = form.cleaned_data['origin_lat']
            origin_location.long = form.cleaned_data['origin_lng']
            origin_location.state = form.cleaned_data['origin_state']
            origin_location.country = form.cleaned_data['origin_country']
            origin_location.start_date = form.cleaned_data['start_date']
            origin_location.meeting_point = form.cleaned_data['meeting_point']
            origin_location.trip = trip
            origin_location.save()

            trip.origin = origin_location.pk
            trip.start_date = form.cleaned_data['start_date']
            trip.save()

            destination_location = Location(name=form.cleaned_data['destination_input'])
            destination_location.lat = form.cleaned_data['destination_lat']
            destination_location.long = form.cleaned_data['destination_lng']
            destination_location.state = form.cleaned_data['destination_state']
            destination_location.country = form.cleaned_data['destination_country']
            destination_location.start_date = form.cleaned_data['finish_date']
            destination_location.photo_url = form.cleaned_data['photo_url']
            destination_location.trip = trip
            destination_location.parent = origin_location.pk
            destination_location.save()

            trip.destination = destination_location.pk
            trip.finish_date = form.cleaned_data['finish_date']
            list_route = [origin_location.pk, destination_location.pk]
            trip.route = '-'.join(map(str, list_route))
            trip.followers.add(request.user)
            trip.num_followers = 1
            trip.save()

            return HttpResponseRedirect(reverse('trips:details', args=(trip.pk,)))
        else:
            data = {'form': form}
            return render(request, 'trips/new_trip.html', data)
    else:
        data = {'form': NewTripForm()}
    return render(request, 'trips/new_trip.html', data)


@login_required
def trip_list(request):
    trips = Trip.objects.all().order_by('-start_date', '-id')
    locations = Location.objects.all().order_by('-id')

    list_trips = []
    for trip in trips:
        route = trip.route
        if route:
            route = route.split('-')
        else:
            route = []

        origin_name = ''
        destination_name = ''

        start_date = trip.start_date
        start_date = start_date.strftime("%d %B %Y %H:%M")
        finish_date = trip.finish_date
        finish_date = finish_date.strftime("%d %B %Y %H:%M")
        for location in locations:
            if len(route):
                for i in range(len(route)):
                    if int(route[i]) == location.id:
                        route[i] = location.name
                        break

            if trip.origin == location.id:
                origin_name = location.name
            if trip.destination == location.id:
                destination_name = location.name
            if origin_name and destination_name:
                break

        if len(route):
            route = '<br><i class="fa fa-fw fa-arrow-right"></i> '.join(map(str, route))
        else:
            route = ''
        list_trip = {'id': trip.id, 'origin_name': origin_name, 'destination_name': destination_name,
                     'start_date': start_date, 'finish_date': finish_date, 'route': route}
        list_trips.append(list_trip)

    data = {'trips': list_trips}
    return render(request, 'trips/trip_list.html', data)


@login_required
def details(request, trip_id):
    try:
        trip_id = int(trip_id)
    except ValueError:
        trip_id = 0
    locations = Location.objects.filter(trip__pk=trip_id)
    if locations:
        dict_location = {}
        for location in locations:
            dict_location[str(location.id)] = location

        trip = locations[0].trip
        destination_location = dict_location[str(trip.destination)]
        num_followers = trip.num_followers
        origin = trip.origin
        destination = trip.destination
        route = trip.route
        if route:
            route = route.split('-')
        else:
            route = []
        locations_route = []
        for i in route:
            locations_route.append(dict_location[str(i)])

        is_creator = False
        has_joined = False
        if trip.creator == request.user:
            is_creator = True
        already_join = Trip.objects.filter(pk=trip_id, followers=request.user)
        if already_join:
            has_joined = True

        data = {'num_followers': '{:,}'.format(num_followers), 'origin': origin, 'destination': destination,
                'destination_location': destination_location, 'trip_id': trip_id, 'is_creator': is_creator,
                'has_joined': has_joined, 'locations_route': locations_route}
        return render(request, 'trips/details.html', data)
    else:
        raise Http404("Trip does not exist")


def join(request):
    try:
        trip_id = int(request.POST.get('id', ''))
    except ValueError:
        trip_id = 0
    trip = Trip.objects.filter(pk=trip_id)
    if trip:
        already_join = trip.filter(followers=request.user)
        if already_join:
            status = 'ok'
            message = "You've already joined this trip."
        else:
            trip[0].followers.add(request.user)
            num_followers = trip[0].num_followers
            trip[0].num_followers = num_followers + 1
            trip[0].save()

            if trip.filter(followers=request.user):
                status = 'ok'
                message = 'You are now joining this trip.'
            else:
                status = 'error'
                message = 'A database error occured. Please try again.'
    else:
        status = 'error'
        message = 'Specified trip is not found.'
    data = {'status': status, 'message': message}
    return JsonResponse(data)
