import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORM.settings')
import django
django.setup()

from myapplication.models import EmployeeModel
from faker import Faker
f = Faker()

def populate_data(n):
    for i in range(n):
        ename = f.name()
        email = f.email()
        city = f.city()
        address = f.address()
        company = f.company()
        salary = f.random_int(min=10000, max=70000)
        jobrole = f.job()

        EmployeeModel.objects.create(
            ename=ename, 
            email=email, 
            city=city, 
            address=address, 
            company=company, 
            salary=salary, 
            jobrole=jobrole
        )

n = int(input("Enter the no.of records: "))
populate_data(n)
print(f"{n} records created successfully.")
