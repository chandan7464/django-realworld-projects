from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def attendance_view(request):
    return HttpResponse("Attendance View")  
def exam_view(request):
    return HttpResponse("Exam View")  
def timetable_view(request):
    return HttpResponse("Timetable View")

