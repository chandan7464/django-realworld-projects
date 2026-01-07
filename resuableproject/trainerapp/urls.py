
from django.urls import path
from trainerapp import views
urlpatterns = [
    path('sylabus/',views.syllabus_view),
    path('result/', views.result_view),
    path('leave/', views.leav_view),
    
]
