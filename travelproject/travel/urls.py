from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.sign_in, name="sign-in"),
	path('sign-up', views.sign_up, name="sign-up"),
	path('sign-out', views.sign_out, name="sign-out"),
	path('forgotten-password', views.forgotten_password, name="forgotten-password"),
	path('email', views.email, name="email"),
	path('account', views.account, name="account"),
	path('profile', views.profile, name="profile"),
	path('verification', views.verification, name='verification'),
]