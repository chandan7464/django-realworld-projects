from django.urls import path
from newsapp import views
urlpatterns=[
   path('',views.home_views,name="home"),
   path('business/',views.business_views,name="business"),
   path('sports/',views.sports_views,name="sports"),
   path('entertainment/',views.entertainment_views,name="entertainment"),
]