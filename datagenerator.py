import json
import random
from faker import Faker

fake = Faker()

employees = []
restaurants = []

for i in range(1, 5000):
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

    

    restaurant = {
        "model": "obapp.employee",  # Replace 'yourappname' with your actual app name
        "pk": i,
        "fields": {
            "name": fake.name(),
            "address":fake.address(),
            "res_type":random.choice(['IN','CH','IT','GR','MX','FF','OT'])
        }
    }
    restaurants.append(restaurant)

with open('restaurants.json', 'w') as f:
    json.dump(restaurants, f, indent=4)


with open('employees.json', 'w') as f:
    json.dump(employees, f, indent=4)

print("Generated employees.json with 5000 records.")
