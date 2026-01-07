from django.urls import path
from studentapp import views

urlpatterns = [
    path('attendance/', views.attendance_view),
    path('exam/', views.exam_view),
    path('time/', views.timetable_view),
]
