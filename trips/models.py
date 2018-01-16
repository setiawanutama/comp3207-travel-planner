from django.conf import settings
from django.db import models


class Trip(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator')
    origin = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField()
    destination = models.IntegerField(null=True, blank=True)
    finish_date = models.DateTimeField()
    route = models.TextField()  # will serve as list of locations
    num_followers = models.IntegerField(default=0)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Location(models.Model):
    name = models.CharField(max_length=300)
    lat = models.DecimalField(null=False, max_digits=10, decimal_places=8)
    long = models.DecimalField(null=False, max_digits=11, decimal_places=8)
    start_date = models.DateTimeField()
    photo_url = models.CharField(max_length=200, blank=True)
    meeting_point = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    parent = models.IntegerField(null=True, blank=True)
