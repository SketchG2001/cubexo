from django.urls import path
from . import views


urlpatterns = [
    path("",views.home_page,name="index"),
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile")
]