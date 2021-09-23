from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TimeField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(verbose_name="Address", max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name="City", max_length=100, null=True, blank=True)
    zip_code = models.CharField(verbose_name="Zip Code", max_length=5, null=True, blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, null=True, blank=True)
    signup_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Guest(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=20)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=200)
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

class Booking(models.Model):
    # guest_name=models.CharField(max_length=200)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(default=datetime.now())
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
                # return total_cost
                return total_cost
        else:
            return 'calculated when checked out'        
    
@receiver(post_save,sender=Booking)
def  RType(sender, instance, created, **kwargs):
    room = instance.room
    if created:
        room.is_available = False
    room.save()
    if instance.check_out ==True:
        room.is_available=True
    room.save()    
    


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
