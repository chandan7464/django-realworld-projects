from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    return HttpResponse("Register View")
def login_view(request):
    return HttpResponse("Login View")
def logout_view(request):
    return HttpResponse("Logout View")
