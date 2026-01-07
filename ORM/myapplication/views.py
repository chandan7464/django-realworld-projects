from django.shortcuts import render
from django.http import HttpResponse
from myapplication.models import EmployeeModel

# Create your views here.
def employee_view(request):
    all_data = EmployeeModel.objects.all().order_by('id')
    context = {
        "employee_data": all_data
    }
    return render(request, 'employee_data.html', context)

    
