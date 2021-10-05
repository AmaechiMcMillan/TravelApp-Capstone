from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date,timedelta, timezone
from django.db.models.expressions import F
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import datetime, now

class TravelProfile(models.Model):
	
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone_number = models.CharField(max_length=15, null=True, blank=True)         
    dob = models.DateField()
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name="City",max_length=100, null=True, blank=True)
    zip_code = models.CharField(verbose_name="Zip Code",max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
	
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
	
    is_active = models.BooleanField(default = True)
    
    email_verified = models.BooleanField(default = False)
    has_profile = models.BooleanField(default=False)

    def __str__(self):
	    return f'{self.user}'


class UserToken(models.Model):
	
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	token = models.CharField(max_length=100, null=True, blank=True) 
	is_email = models.BooleanField(default= False)
	is_password = models.BooleanField(default = False)

	is_active = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.user}'

class Guest(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    city= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no=models.IntegerField(default=101)
    hotel = models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
    room_type=models.CharField(max_length=200,default='standard')
    rate = models.FloatField()
    is_available = models.BooleanField(default=True)
    no_of_beds = models.IntegerField(default=3)
    # check_out=models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.room_no)


    def hotel_name(self):
        return self.hotel.name

class HotelBooking(models.Model):
    #guest_name=models.CharField(max_length=200)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    checkout_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    check_out=  models.BooleanField(default=False)
    no_of_guests = models.IntegerField(default=1)

    def __str__(self):
        return self.guest.name

    def charge(self):
        if self.check_out:
            if self.checkin_date==self.checkout_date:
                return self.room.rate
            else:
                time_delta = self.checkout_date - self.checkin_date
                total_time = time_delta.days
                total_cost =total_time*self.room.rate
                return total_cost
        else:
            return 'calculated when checked out'

class Flight(models.Model):
    name = models.CharField(max_length=50)
    city= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Seating(models.Model):
    flight_no=models.IntegerField(default=101)
    flight = models.ForeignKey(Hotel,null=True,on_delete=models.CASCADE)
    seat_type=models.CharField(max_length=200,default='standard')
    rate = models.FloatField()
    is_available = models.BooleanField(default=True)
    no_of_seats = models.IntegerField(default=3)

    def __str__(self):
        return str(self.flight_no)


    def hotel_name(self):
        return self.flight.name

class FlightBooking(models.Model):
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    seating = models.ForeignKey(Seating,on_delete=models.CASCADE)
    no_of_passengers = models.IntegerField
    departing_from = models.CharField(max_length=50)
    arriving_to = models.CharField(max_length=50)
    leave_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    return_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    returning = models.BooleanField(default=False)

    def __str__(self):
        return self.passenger

    def charge(self):
        if self.returning:
            if self.arriving_to==self.departing_from:
                return self.flight.rate
            else:
                time_delta = self.departing_from - self.arriving_to
                total_time = time_delta.days
                total_cost =total_time*self.flight.rate
                # return total_cost
                return total_cost
        else:
            return 'calculated when returned'
    
