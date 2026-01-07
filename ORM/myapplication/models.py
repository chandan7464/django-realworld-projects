from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
      ename=models.CharField(max_length=50)
      email=models.EmailField()
      city=models.CharField(max_length=100)
      address=models.TextField()
      company=models.CharField(max_length=100)
      salary=models.IntegerField()
      jobrole=models.CharField(max_length=100)