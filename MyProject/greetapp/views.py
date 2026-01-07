from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def wish_view(request): 
    hr = datetime.datetime.now().hour
    if hr < 12:
        msg = "Good Morning"
    elif hr < 16:
        msg = "Good Afternoon"
    elif hr < 20:
        msg = "Good Evening"
    else:
        msg = "Good Night"
    return HttpResponse(f"<h1>{msg}</h1><br>Current Time is {datetime.datetime.now()}")