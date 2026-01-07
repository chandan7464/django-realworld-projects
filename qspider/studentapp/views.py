from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def attendance_view(request):
    return HttpResponse("This is attendance View") 
 
def exam_view(request):
    return render(request,"studentapp/exam.html")
  
def timetable_view(request):
    return HttpResponse("This is timetable View")

def student_view(request):

    student_data = {
        'name': 'python',
        'subject': 'numpy',
        'address': 'noida',
        'pin': 201301

    }


    return render(request,"student.html",student_data)




