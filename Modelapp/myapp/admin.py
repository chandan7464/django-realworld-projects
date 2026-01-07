from django.contrib import admin
from myapp.models import StudentModel
# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','rollno','subject','address','email','is_active']


admin.site.register(StudentModel,StudentModelAdmin)
