from django import forms

# from .models import Trip, Location, Join

class NewTripForm(forms.Form):
	origin_input = forms.CharField(max_length=300, strip=True, widget=forms.TextInput(attrs={'id': 'origin-input', 'class': 'form-control', 'placeholder': 'Enter an origin location'}))
	origin_name = forms.CharField(max_length=200, strip=True, widget=forms.HiddenInput(attrs={'data-geo': 'name'}))
	origin_lat = forms.DecimalField(widget=forms.HiddenInput(attrs={'data-geo': 'lat'}))
	origin_lng = forms.DecimalField(widget=forms.HiddenInput(attrs={'data-geo': 'lng'}))
	origin_state = forms.CharField(max_length=50, strip=True, required=False, widget=forms.HiddenInput(attrs={'data-geo': 'administrative_area_level_1'}))
	origin_country = forms.CharField(max_length=50, strip=True, required=False, widget=forms.HiddenInput(attrs={'data-geo': 'country'}))
	start_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.TextInput(attrs={'id': 'start_date', 'class': 'form-control', 'placeholder': 'Pick start date & time'}))
	destination_input = forms.CharField(max_length=300, strip=True, widget=forms.TextInput(attrs={'id': 'destination-input', 'class': 'form-control', 'placeholder': 'Enter an destination location'}))
	destination_name = forms.CharField(max_length=200, strip=True, widget=forms.HiddenInput(attrs={'data-geo': 'name'}))
	destination_lat = forms.DecimalField(widget=forms.HiddenInput(attrs={'data-geo': 'lat'}))
	destination_lng = forms.DecimalField(widget=forms.HiddenInput(attrs={'data-geo': 'lng'}))
	destination_state = forms.CharField(max_length=50, strip=True, required=False, widget=forms.HiddenInput(attrs={'data-geo': 'administrative_area_level_1'}))
	destination_country = forms.CharField(max_length=50, strip=True, required=False, widget=forms.HiddenInput(attrs={'data-geo': 'country'}))
	finish_date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.TextInput(attrs={'id': 'finish_date', 'class': 'form-control', 'placeholder': 'Pick finish date & time'}))
	photo_url = forms.URLField(max_length=200, required=False, widget=forms.URLInput(attrs={'id': 'photo_url', 'class': 'form-control', 'placeholder': 'Enter image URL'}))
	meeting_point = forms.CharField(max_length=100, strip=True, required=False, widget=forms.TextInput(attrs={'id': 'meeting_point', 'class': 'form-control', 'placeholder': 'Enter a meeting point location'}))