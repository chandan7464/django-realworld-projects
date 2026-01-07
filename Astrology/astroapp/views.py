from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random


#create your view here
def horoscope_view(request):
    hr = datetime.datetime.now().time().hour
    if hr < 12:
        msg = 'morning'
    elif hr <16:
        msg = 'Afternoon'
    elif hr<21:
        msg = 'Evening'
    else:
        msg = 'Night'
    list1  = [
             'Golden days ahead',
             'Very soon you will get a job',
             'spray water to reduce AQI',
             'Watch reels before sleep',
             
    ]                
    name_list = ['chandan','yash','nitesh','rupesh','summit','Hemant']
    candidate_list=['sri','devi','lora']

    s = random.choice(list1)
    name = random.choice(name_list)
    candidate = random.choice(candidate_list)
  
    my_dict ={
       'wish':msg,
        'message':s,
        'name':name,
        'candidate':candidate
    }
    return render(request,'astroapp/horoscope.html',my_dict)
def home_view(request):
    return render(request,'astroapp/home.html')

