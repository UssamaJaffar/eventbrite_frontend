from django.urls import path

from .views import Events , CreateEvents , CreateVenue

urlpatterns = [
    path('', Events),
    path('create-events/', CreateEvents),
    path('create-venue/', CreateVenue),


]
