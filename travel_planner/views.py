from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, views as auth_views

from trips.models import Trip, Location

def index(request):
    trips = Trip.objects.all().order_by('-start_date', '-id')
    locations = Location.objects.all().order_by('-id')

    list_trips = []
    for trip in trips:
        destination_name = ''

        start_date = trip.start_date
        start_date = start_date.strftime("%d %B %Y %H:%M")
        finish_date = trip.finish_date
        finish_date = finish_date.strftime("%d %B %Y %H:%M")
        for location in locations:
            if trip.destination == location.id:
                destination_name = location.name
                country = location.country
                photo_url = location.photo_url
                break
        list_trip = {'id': trip.id, 'destination_name': destination_name,
                     'country': country, 'photo_url': photo_url}
        list_trips.append(list_trip)
    data = {'trips': list_trips}
    return render(request, 'index.html', data)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/trips/')
    else:
        return auth_views.login(request)


def signout(request):
    logout(request)
    return auth_views.login(request)


@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except ValueError:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'trips/settings.html', {'facebook_login': facebook_login, 'can_disconnect': can_disconnect})


@login_required
def password(request):
    if request.user.has_usable_password():
        password_form = PasswordChangeForm
    else:
        password_form = AdminPasswordChangeForm

    if request.method == 'POST':
        form = password_form(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = password_form(request.user)
    return render(request, 'trips/password.html', {'form': form})
