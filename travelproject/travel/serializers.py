from django.db.models import fields
from django.db.models.query_utils import FilteredRelation
from rest_framework import serializers
from .models import TravelProfile
from .models import Guest
from .models import Hotel
from .models import Room
from .models import HotelBooking
from .models import Flight
from .models import Passenger
from .models import Seating
from .models import FlightBooking


class TravelProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProfile
        fields = ['id', 'user_id', 'phone_number', 'dob', 'address', 'city', 'zip_code', 'country']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'name', 'age', 'phone_number']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'phone_number', 'city']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'hotel_id', 'room_no', 'room_type', 'rate', 'is_available', 'no_of_beds']

class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = ['id', 'room_id', 'guest_id', 'hotel_id', 'chechin_date',  'checkout_date', 'checkout', 'no_of_guests']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'name', 'city']

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'age', 'phone_number']

class SeatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seating
        fields = ['id', 'flight_no', 'flight_id', 'seat_type', 'rate', 'is_available', 'no_of_seats']

class FlightBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightBooking
        fields = ['id', 'flight_id', 'passenger_id', 'seating_id', 'no_of_passengers', 'departing_to', 'arriving_to', 'leave_date', 'return_date', 'returning']




