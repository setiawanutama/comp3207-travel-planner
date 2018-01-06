from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/', admin.site.urls),
	
	url(r'^trips/', include('trips.urls')),

    url(r'^login/$', views.login, name='login'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
	
	url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
]