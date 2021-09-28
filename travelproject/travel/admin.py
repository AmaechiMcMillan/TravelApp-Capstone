from django.contrib import admin
from .models import HotelBooking, UserProfile
from .models import Guest
from .models import Hotel
from .models import Room
from .models import FlightBooking
from .models import Flight
from .models import Passenger
from .models import Seating


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelBooking)
admin.site.register(FlightBooking)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Seating)