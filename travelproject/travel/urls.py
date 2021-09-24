from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    path('index', views.index, name="index")
]