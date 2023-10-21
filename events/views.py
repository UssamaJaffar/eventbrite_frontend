from django.shortcuts import render
from .forms import EventForm ,VenueForm

from Event_Management.settings import API_URL

from utils.Decorators.decorators import authentication_required

import requests
import json

@authentication_required
def Events(request):
    response = None
    res = requests.get(API_URL+'/user/login/', headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
    
    if res.status_code == 200:
        response = res.json()

    return render(request,'event.html',{'response': response})

@authentication_required
def CreateEvents(request):
    if request.method == 'GET':
        form = EventForm([])
        return render(request, 'CreateEvent.html',{"form":form})

    elif request.method == 'POST':
        form = EventForm([],request.POST)
        if form.is_valid():
            pass

        return render(request , 'CreateEvent.html',{"form":form})
    
    return render(request,'CreateEvent.html',{'form':form})

@authentication_required
def CreateVenue(request):
    if request.method == 'GET':
        form = VenueForm()
        return render(request, 'CreateVenue.html',{"form":form})
    
    elif request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            pass

        return render(request , 'CreateVenue.html',{"form":form})
    
    return render(request,'CreateVenue.html',{'form':form})