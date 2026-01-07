from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import StudentModel

# Create your views here.
def student_view(request):
    all_data = StudentModel.objects.all()
    context = {"student_data":all_data}
    return render(request,'student_data.html',context)



