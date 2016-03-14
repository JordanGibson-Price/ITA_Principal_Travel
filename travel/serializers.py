from .models import Trip, Event, Principal
from cities_light.models import Country
from rest_framework import serializers

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class EventSerializer(serializers.ModelSerializer):
    cities_light_country = CountrySerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class TripSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)
    class Meta:
        model = Trip
        fields = '__all__'
