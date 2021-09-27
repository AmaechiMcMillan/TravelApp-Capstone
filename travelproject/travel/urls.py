from django.urls import path
from . import views

app_name = 'travel'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:profile_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_profile')
]