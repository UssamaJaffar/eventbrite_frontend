from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SignUpForm , loginForm

from Event_Management.settings import API_URL

from django.contrib import messages

from utils.Decorators.decorators import authentication_not_required

import requests
import json
# Create your views here.

@authentication_not_required
def login(request):
    if request.method == 'GET':
        form = loginForm
        return render(request , 'login.html',{"form":form})
    
    elif request.method == 'POST':
        form = loginForm(request.POST)
    
        if form.is_valid():
    
            jsn = {"email":form.data['Email'],"password":form.data['Password']}
            res = requests.post(API_URL+'/user/login/', data=json.dumps(jsn), headers={"Content-Type":"application/json"})
    
            if res.status_code == 200:
    
                tokens = res.json().get('tokens')
                request.session['access_token'] = tokens['refresh']
                request.session['refresh_token'] = tokens['access']
    
                return redirect('/event/')

            messages.error(request , res.json().get('Message'))
            return render(request , 'login.html',{"form":form})
             
        return render(request , 'login.html',{"form":form})

    form = loginForm
    return render(request , 'login.html',{"form":form})

@authentication_not_required
def Register(request):

    if request.method == 'GET':
        form = SignUpForm
        return render(request , 'Sign_Up.html',{"form":form})
    
    elif request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():

            jsn = {"email":form.data['Email'],"password":form.data['Password'], "fullname": form.data['Full_Name']}
            res = requests.post(API_URL+'/user/registeruser/', data=json.dumps(jsn), headers={"Content-Type":"application/json"})
    
            if res.status_code == 200:
                return redirect('/user/login/')

            messages.error(request , res.json().get('Message'))
            return render(request , 'login.html',{"form":form})

    
        return render(request , 'Sign_Up.html',{"form":form})

    form = SignUpForm
    return render(request , 'Sign_Up.html',{"form":form})
