from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.sign_in, name="sign-in"),
	url(r'^sign-up', views.sign_up, name="sign-up"),
	url(r'^sign-out', views.sign_out, name="sign-out"),
	url(r'^forgotten-password', views.forgotten_password, name="forgotten-password"),
	url(r'^email', views.email, name="email"),
	url(r'^account', views.account, name="account"),
	url(r'^profile', views.profile, name="profile"),
	url(r'^verification/(?P<uidb64>.+)/(?P<token>.+)/$',views.verification, name='verification'),

]