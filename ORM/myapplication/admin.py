from django.contrib import admin
from myapplication.models import EmployeeModel

# Register your models here.
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=['ename','email','city','address','company','salary','jobrole']
admin.site.register(EmployeeModel,EmployeeModelAdmin)   
