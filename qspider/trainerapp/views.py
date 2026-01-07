from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def syllabus_view(request):
    return HttpResponse("This is syllabus View")

def result_view(request):
    return HttpResponse("This is result View")

def leave_view(request):
    return HttpResponse("This is leave View")