"""travelproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from travel.views import home_view, signup_view, activate
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('travel/', include('travel.urls')),
    path('activate/<slug:uidb64>/<slud:token>/', activate, name="activate"),
    path('', RedirectView.as_view(url='travel/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)