from django.shortcuts import render
from .models import Employee,Ratings,Restaurant,Sales
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Avg,Count,Sum
from .utils import email_sender
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView,FormView,DeleteView
from .forms import EmployeeForm,RestForm
import json



# class based views
class RestaurantList(ListView):
    model = Restaurant
    context_object_name = 'object_list'
    paginate_by = 15

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset = queryset.prefetch_related('ratings','sales')
        return queryset


class UpdateRestaurant(UpdateView):
    model = Restaurant
    fields =[
        'name',
        'address'
    ]
    success_url = "/"


class UpdateEmployee(UpdateView):
    model = Employee
    fields = [
        'name',
        'salary',
        'mobile',
        'email'
    ]
    success_url = '/'


class EmployeeFormView(FormView):
    # model = Employee
    form_class = EmployeeForm
    template_name = 'obapp/employee_create_form.html'
    success_url = '/'

    def form_valid(self, form):
        emp_instance = Employee(**form.cleaned_data)
        emp_instance.save()
        return super().form_valid(form)


class CreateRestaurant(FormView):
    form_class= RestForm
    template_name='obapp/create_restaurant_form.html'
    success_url='all-rest'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'obapp/employee_confirm_delete.html'
    success_url = "/create-emp"




def send_mes(email):
    template = "test_email.html"
    context = {
        'subject':"this is test email",
        'to_email':email,
        'attachment': os.path.join('onboard/staticfiles/img/sample.jpg')
    }

    email_sender(template ,context=context)



def load_data_from():
    with open('/home/my/Desktop/onboarding/onboard/employees.json', 'r') as file:
        data = json.load(file)
        return data
def load_restaurant_data():
    with open('/home/my/Desktop/onboarding/onboard/restaurants.json', 'r') as file:
        data = json.load(file)
        return data

def home_page(request):
    # dataset = load_data_from()
    # for data in dataset:
    #     Employee.objects.create(name=data['fields']['name'],salary=data['fields']['salary'],mobile=data['fields']['mobile'],
    #                             email=data['fields']['email'],city=data['fields']['city'],country=data['fields']['country'])
    employees = Employee.objects.all()


    summary = employees.aggregate(
        total_emp = Count('id')
    )
    print("total employee: ",summary)
    p = Paginator(employees,15)
    page_num = request.GET.get('page')
    try:
        page_ojb = p.get_page(page_num)
    except PageNotAnInteger:
        page_ojb = p.page(1)
    except EmptyPage:
        page_ojb = p.page(p.num_pages)
    context = {
        'page_obj':page_ojb
    }
    return render(request,'home.html',context)


def restaurant(request):
    # loading restaurants data
    # dataset = load_restaurant_data()
    
    # for data in dataset:
    #     Restaurant.objects.create(
    #         name=data['fields']['name'],
    #         address=data['fields']['address'],
    #         res_type=data['fields']['res_type']
    #     )
    

    #  prefetch related

    # restaturants = Restaurant.objects.prefetch_related('ratings','sales')
    # context = {
    #     'restaurants':restaturants
    # }


    # select related

    ratings = Ratings.objects.only('restaurant__name','rating').select_related('restaurant')

    # Reverse foreign key lookup 
    restaurants = Restaurant.objects.first()
    sales = restaurants.sales.all()
    print(sales)
    

    context = {
        'ratings':ratings
    }
    email = "vikasgole089@gmail.com"
    send_mes(email=email)

    return render(request,'restaurant.html',context)


