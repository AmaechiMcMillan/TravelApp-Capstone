from django.contrib import admin
from .models import Booking, Profile
from .models import Guest
from .models import Hotel
from .models import Room
from .models import Booking


# Register your models here.
admin.site.register(Profile)
admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)