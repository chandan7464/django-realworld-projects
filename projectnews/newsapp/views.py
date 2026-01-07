from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_views(request):
    return render(request,'newsapp/home.html')
def business_views(request):
    h1="share market price up and down"
    h2="trading is a game of big player"
    h3="zerodha  is traiding platfrom "
    type='business'
    mydict={'type':type,'h1':h1,'h2':h2,'h3':h3}
    return render(request,'newsapp/news.html',context= mydict)
def sports_views(request):
    h1="virat kholi plays at no.3"
    h2="virat kholi is king"
    h3="rcb ee sala cup namdu"
    type='sports'
    mydict={'type':type,'h1':h1,'h2':h2,'h3':h3}
    return render(request,'newsapp/news.html',context= mydict)
def entertainment_views(request):
    h1="Bollywood is shit"
    h2="Tony stark"
    h3="south movie  has a best script"
    type='entertainment'
    mydict={'type':type,'h1':h1,'h2':h2,'h3':h3}
    return render(request,'newsapp/news.html',context= mydict)


