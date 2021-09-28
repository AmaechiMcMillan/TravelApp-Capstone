from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms import ModelForm 
from .models import UserProfile, UserToken

class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )


class AuthForm(AuthenticationForm):
	
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )



class UserProfileForm(forms.ModelForm):

	phone_number = forms.CharField(max_length=15, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Phone Number..'}))
	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	city = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	zip_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('phone_number', 'address', 'city', 'zip_code', 'country', 'longitude', 'latitude')



class RequestPasswordForm(PasswordResetForm):
	
	email = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	
	class Meta:
		model = User
		fields = ('email',)



class ForgottenPasswordForm(SetPasswordForm):
	
	new_password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	new_password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('password1', 'password2', )