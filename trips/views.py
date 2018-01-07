from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def dashboard(request):
	data = {}
	return render(request, 'trips/dashboard.html', data)

@login_required
def add_new_trip(request):
	data = {}
	return render(request, 'trips/new_trip.html', data)

@login_required
def list(request):
	data = {}
	return render(request, 'trips/trip_list.html', data)

@login_required
def details(request):
	data = {}
	return render(request, 'trips/details.html', data)