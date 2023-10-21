from django.shortcuts import render
from .forms import EventForm ,VenueForm

from Event_Management.settings import API_URL

from utils.Decorators.decorators import authentication_required

from django.shortcuts import redirect
from django.contrib import messages

from datetime import datetime

import requests
import json

@authentication_required
def Events(request):
    response = None
    res = requests.get(API_URL+'/event/event/', headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
    
    if res.status_code == 200:
        response = res.json()

    elif res.status_code == 401:
        request.session['access_token'] = None
        request.session['refresh_token'] = None
        return redirect('/user/login/')
    
    return render(request,'event.html',{'response': response})

@authentication_required
def CreateEvents(request):
    response = None
    res = requests.get(API_URL+'/event/veune/', headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
    
    if res.status_code == 200:
        response = res.json()
    elif res.status_code == 401:
        request.session['access_token'] = None
        request.session['refresh_token'] = None
        return redirect('/user/login/')
        
    if request.method == 'GET':
        veunes = []
        for veune in response:
            veunes.append((veune['Venue_id'],veune['name']))
        form = EventForm(veunes)
        return render(request, 'CreateEvent.html',{"form":form})

    elif request.method == 'POST':
        veunes = []
        for veune in response:
            veunes.append((veune['Venue_id'],veune['name']))

        form = EventForm(veunes,request.POST)
        
        if form.is_valid():
            start_date = form.data['start_date'].split('T')
            end_date = form.data['end_date'].split('T')
            start_date = datetime.strptime(start_date[0] + ' '+ start_date[1], '%Y-%m-%d %H:%M')
            end_date = datetime.strptime(end_date[0] + ' '+ end_date[1], '%Y-%m-%d %H:%M')
            jsn = {
                    "event": {
                        "name": {
                            "html": f"<p>{form.data['name']}</p>"
                        },
                        "description": {
                            "html": f"<p>{form.data['description']}</p>"
                        },
                        "start": {
                            "timezone": "UTC",
                            "utc": start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
                        },
                        "end": {
                            "timezone": "UTC",
                            "utc": end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
                        },
                        "currency": form.data['currency'],
                        "online_event": False,
                        "listed": False,
                        "shareable": False,
                        "invite_only": False,
                        "show_remaining": False,
                        "capacity": form.data['capacity'],
                        "venue_id": form.data['venue_id'],
                        "show_pick_a_seat": True,
                        "show_seatmap_thumbnail": True,
                        "show_colors_in_seatmap_thumbnail": True,
                    },
                    "ticket_class": {
                        "quantity_total": form.data['capacity'],
                        "cost": f"{form.data['currency']},{form.data['cost']}",
                        "name": form.data['Ticket_Name']
                    }
                }
            res = requests.post(API_URL+'/event/event/', data=json.dumps(jsn), headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
            
            if res.status_code == 200:
                return redirect('/event/')
            elif res.status_code == 401:
                request.session['access_token'] = None
                request.session['refresh_token'] = None
                return redirect('/user/login/')
            
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
            jsn = {
                    "venue": {
                        "name": form.data['address_place'],
                        "capacity": form.data['capacity'],
                        "address": {
                        "address_1": form.data['address_place'],
                        "latitude" : form.data['latitude'],
                        "longitude": form.data['longitude']
                        }
                    }
                }
            res = requests.post(API_URL+'/event/veune/', data=json.dumps(jsn), headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
            
            if res.status_code == 200:
                return redirect('/event/')
            elif res.status_code == 400:
                messages.error(request , res.json()['response']['error_description'])
        
        return render(request , 'CreateVenue.html',{"form":form})
    
    return render(request,'CreateVenue.html',{'form':form})


@authentication_required
def EventDetail(request, id):
    response = None
    res = requests.get(API_URL + f'/event/event/{id}/', headers={"Content-Type":"application/json", "Authorization" : "Bearer "+request.session['access_token']})
    
    if res.status_code == 200:
        response = res.json()
    elif res.status_code == 401:
        request.session['access_token'] = None
        request.session['refresh_token'] = None
        return redirect('/user/login/')
    
    return render(request,'Event_detail.html',{'response':response['response']})