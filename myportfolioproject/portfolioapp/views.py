from django.shortcuts import render

# Create your views here.
def base_views(request):
    return render(request,'portfolioapp/base.html')
def home_views(request):
    return render(request, 'portfolioapp/home.html')

def about_views(request):
    return render(request, 'portfolioapp/about.html')

def contact_views(request):
    return render(request, 'portfolioapp/contact.html')

def gallery_views(request):
    return render(request, 'portfolioapp/gallery.html')
