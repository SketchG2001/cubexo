from django.urls import path
from .views import index,PublisherDocument


urlpatterns = [
    path('', index, name='index'),
    path('search/',PublisherDocument.as_view({'get':'list'})),
]