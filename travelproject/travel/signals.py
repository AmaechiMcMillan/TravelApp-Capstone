from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import TravelProfile
from . models import HotelBooking
from . models import FlightBooking


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userprofile = TravelProfile.objects.create(user=instance)


@receiver(post_save,sender=HotelBooking)
def  RType(sender, instance, created, **kwargs):
    room = instance.room
    if created:
        room.is_available = False
    room.save()
    if instance.check_out ==True:
        room.is_available=True
    room.save()    


@receiver(post_save,sender=FlightBooking)
def RType(sender, instance, created, **kwargs):
    flight = instance.flight
    if created:
        flight.is_available = False
    flight.save()
    if instance.returning ==True:
        flight.is_available=True
    flight.save()
    


#@receiver(post_save, sender=User)
#def update_profile_signal(sender, instance, created, **kwargs):
#    if created:
#        UserProfile.objects.create(user=instance)
#    instance.user_profile.save()
