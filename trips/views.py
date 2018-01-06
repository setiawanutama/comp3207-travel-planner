from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def dashboard(request):
	full_name = request.user.get_full_name()
	data = {
		'full_name': full_name,
	}
	return render(request, 'trips/dashboard.html', data)

@login_required
def details(request):
	full_name = request.user.get_full_name()
	data = {
		'full_name': full_name,
	}
	return render(request, 'trips/details.html', data)