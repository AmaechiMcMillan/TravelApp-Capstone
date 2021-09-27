from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from .models import Profile, HotelBooking, FlightBooking
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView 
from rest_framework_api_key.permissions import HasAPIKey
from django.urls import reverse


def index(request):
    all_profiles = Profile.objects.all()
    context = {
        'all_profiles': all_profiles
    }
    all_hotelbookings = HotelBooking.objects.all()
    context = {
        'all_hotelbookings': all_hotelbookings
    }
    all_flightbookings = FlightBooking.objects.all()
    context = {
        'all_flightbookings': all_flightbookings
    }
    return render(request, 'travel/index.html', context)

#def detail(request, profile_id):

def home_view(request):
    return render(request, 'home.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            message = render_to_string('activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserListView(APIView):
    permission_classes = [HasAPIKey]

#def index(request):

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        email = request.POST.get('email')
        phone_number = request.POST.get('number')
        address = request.POST.get('address') 
        city = request.POST.get('city') 
        zip_code = request.POST.get('number')
        country = request.POST.get('country')
        new_profile = Profile(name=name, email=email, phone_number=phone_number, address=address, city=city, zip_code=zip_code, country=country)
        new_profile.save()
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        return render(request, 'profiles/create.html')