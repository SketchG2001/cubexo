import json
from django.conf import settings
from .models import Student
from django.http import JsonResponse


def insert_data():
    with open('D:\multiteant\students.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            student = Student.objects.create(
                name=item['name'],
                age=item['age'],
                email=item['email'],
                city=item['city'],
                mobile=item['mobile'][0:10],
                type=item['type']
            )


def index(request):
    insert_data()
    return JsonResponse({'status': 'success'})
