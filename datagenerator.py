import json
import random
from faker import Faker

fake = Faker()

employees = []

for i in range(1, 101):
    employee = {
        "model": "obapp.employee",  # Replace 'yourappname' with your actual app name
        "pk": i,
        "fields": {
            "name": fake.name(),
            "salary": str(random.randint(30000, 100000)),
            "mobile": fake.msisdn()[0:10],
            "email": fake.unique.email(),
            "city": fake.city(),
            "country": fake.country()
        }
    }
    employees.append(employee)

with open('employees.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Generated employees.json with 100 records.")
