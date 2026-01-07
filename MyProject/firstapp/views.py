from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
# Create your view here.
def date_view(request):
    current_time = datetime.datetime.now()
    return HttpResponse(f"<h1>Current time {current_time}</h1>")
def greet_view(request):
    msg = "Hello Everyone/nGood afternon"
    return HttpResponse(f"<h1>{msg}<h1>")


