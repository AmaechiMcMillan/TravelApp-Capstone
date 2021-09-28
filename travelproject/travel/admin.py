from django.contrib import admin
from .models import HotelBooking, UserProfile, UserToken
from .models import Guest
from .models import Hotel
from .models import Room
from .models import FlightBooking
from .models import Flight
from .models import Passenger
from .models import Seating


# Register your models here.
admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelBooking)
admin.site.register(FlightBooking)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Seating)


#class UserProfileAdmin(admin.ModelAdmin):
    #list_display = ('id', 'user', 'timestamp')
admin.site.register(UserProfile)


#class UserTokenAdmin(admin.ModelAdmin):
    #list_display = ('id', 'user', 'timestamp')
admin.site.register(UserToken)