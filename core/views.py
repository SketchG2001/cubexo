from django.shortcuts import render
from .models import Student
from django_tenants.utils import get_tenant_base_schema
def student_list(request):


    print("public schema:", get_tenant_base_schema())
    students = Student.objects.all()
    return render(request, 'core/students.html', {'students': students})
