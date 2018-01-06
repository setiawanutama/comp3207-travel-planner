# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required
def dashboard(request):
    return render(request, 'trips/dashboard.html')

@login_required
def details(request):
    return render(request, 'trips/details.html')