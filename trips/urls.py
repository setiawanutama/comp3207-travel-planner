from django.conf.urls import url
from . import views as trip_views

urlpatterns = [
    url(r'^$', trip_views.dashboard, name='dashboard'),
	url(r'^new/', trip_views.add_new_trip, name='add_new_trip'),
	url(r'^list/', trip_views.list, name='trip_list'),
	url(r'^details/', trip_views.details, name='details'),
]