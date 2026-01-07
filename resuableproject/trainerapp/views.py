from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def syllabus_view(request):
    return HttpResponse("Syllabus View")

def result_view(request):
    return HttpResponse("Result View")

def leav_view(request):
    return HttpResponse("Leave View")