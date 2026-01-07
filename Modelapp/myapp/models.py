from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    subject=models.CharField(max_length=30)
    address=models.TextField()
    email =models.EmailField()
    is_active=models.BooleanField(default=False)
    
