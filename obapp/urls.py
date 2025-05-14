
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home_page,name='home-page'),
    path("resturant",views.restaurant,name='estaurant'),
    path('all-rest',views.RestaurantList.as_view(),name='all-rest'),
    path('update-rest/<pk>',views.UpdateRestaurant.as_view(),name='update-rest'),
    path('update-emp/<int:pk>',views.UpdateEmployee.as_view(),name='update-emp'),
    path('create-emp',views.EmployeeFormView.as_view(),name='create-emp'),
    path('create-rest',views.CreateRestaurant.as_view(),name='create-rest'),
    path('delete-emp/<int:pk>',views.DeleteEmployee.as_view(),name='delete-emp')

]
