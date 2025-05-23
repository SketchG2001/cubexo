from django.http import  JsonResponse
from .models import ElasticDemo,Car,Product
import  json
from django.conf import settings
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import NewsDocument
from .serializers import NewDocumentSerializer
from django_elasticsearch_dsl_drf.filter_backends import (
 FilteringFilterBackend,
CompoundSearchFilterBackend
)

def generate_random_data():
    with open(settings.BASE_DIR/'news_data.json','r') as f:
        news_data = json.load(f)
    for item in news_data:
        ElasticDemo.objects.create(
            title=item['title'],
            content=item['content']
        )

def generate_car_data():
    with open(settings.BASE_DIR/'car_data.json','r') as f:
        car_data = json.load(f)
        for item in car_data:
            Car.objects.create(
                name=item['name'],
                price=item['price'],
                type=item['type'],
            )
            print("inserted: ",item['type'])

def generate_product_data():
    with open(settings.BASE_DIR/'fake_products.json','r') as f:
        car_data = json.load(f)
        for item in car_data:
            Product.objects.create(
                name=item['name'],
                price=item['price'],
                category=item['category'],
            )
            print("inserted: ",item['category'])


def index(request):
    # generate_random_data()
    # generate_car_data()
    # generate_product_data()
    return JsonResponse({'status': 'success'})



class PublisherDocument(DocumentViewSet):

    document = NewsDocument

    serializer_class = NewDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = ['title', 'content']
    multi_match_search_fields = ['title', 'content']
    filter_fields = {
        'title': 'title',
        'content': 'content',

    }
    fields_fields = {
        'title': 'title',
        'content': 'content',

    }




