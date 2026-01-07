from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register_view(request):
    return render(request,'loginapp/register.html')
def login_view(request):
    return render(request,'loginapp/login.html')
def logout_view(request):
    return render(request,'loginapp/logut.html')
def base_view(request):
    return render(request,'base.html')

