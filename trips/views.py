from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Trip, Location, Join
from .forms import NewTripForm

@login_required
def dashboard(request):
	num_planned_trips = Trip.objects.filter(id = request.user.id)
	num_planned_trips = Trip.objects.count()
	
	num_joined_trips = Join.objects.filter(user = request.user.id)
	num_joined_trips = Join.objects.count()
	
	data = {
		'num_planned_trips': num_planned_trips,
		'num_joined_trips': num_joined_trips,
	}
	return render(request, 'trips/dashboard.html', data)

@login_required
def add_new_trip(request):
	data = {}
	if request.method == 'POST':
		form = NewTripForm(request.POST)
		if form.is_valid():
			trip = Trip(creator = request.user)
			trip.save()
			
			origin_location = Location(name = form.cleaned_data['origin_input'])
			origin_location.lat = form.cleaned_data['origin_lat']
			origin_location.long = form.cleaned_data['origin_lng']
			origin_location.state = form.cleaned_data['origin_state']
			origin_location.country = form.cleaned_data['origin_country']
			origin_location.start_date = form.cleaned_data['start_date']
			origin_location.meeting_point = form.cleaned_data['meeting_point']
			origin_location.trip = trip
			origin_location.save()
			
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
			
			join_trip = Join(user = request.user, trip = trip)
			join_trip.save()
			
			return HttpResponseRedirect(reverse('trips:details', args=(trip.pk,)))
		else:
			data = {'form': form}
			return render(request, 'trips/new_trip.html', data)
	else:
		data = {'form': NewTripForm()}
	return render(request, 'trips/new_trip.html', data)

@login_required
def list(request):
	trips = Trip.objects.all()
	
	
	
	data = {}
	return render(request, 'trips/trip_list.html', data)

@login_required
def details(request, trip_id):
	data = {}
	return render(request, 'trips/details.html', data)