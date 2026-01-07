
from django.urls import path
from trainerapp import views

urlpatterns = [
    path('syllabus/',views.syllabus_view),
    path('result/', views.result_view),
    path('leave/', views.leave_view),
    
]
