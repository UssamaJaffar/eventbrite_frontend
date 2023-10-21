from django.urls import path

from .views import Events , CreateEvents , CreateVenue , EventDetail

urlpatterns = [
    path('', Events),
    path('create-events/', CreateEvents),
    path('create-venue/', CreateVenue),
    path('event_detail/<int:id>/', EventDetail),


]
