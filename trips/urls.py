from django.conf.urls import url
from . import views as trip_views

app_name = 'trips'
urlpatterns = [
    url(r'^$', trip_views.dashboard, name='dashboard'),
	url(r'^new/', trip_views.add_new_trip, name='new'),
	url(r'^list/', trip_views.list, name='trip_list'),
	url(r'^details/(?P<trip_id>\d+)/', trip_views.details, name='details'),
]