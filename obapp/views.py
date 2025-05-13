from django.shortcuts import render
from .models import Employee,Ratings,Restaurant,Sales
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Avg,Count,Sum
from .utils import email_sender
import os
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


def send_mes(email):
    template = "test_email.html"
    context = {
        'subject':"this is test email",
        'to_email':email,
        'attachment': os.path.join('onboard/staticfiles/img/sample.jpg')
    }

    email_sender(template ,context=context)



def home_page(request):
    employees = Employee.objects.all()


    summary = employees.aggregate(
        total_emp = Count('id')
    )
    print("total employee: ",summary)
    p = Paginator(employees,5)
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


