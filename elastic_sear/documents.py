from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Student


@registry.register_document
class StudentDocument(Document):
    class Index:
        name = 'students'  # Name of the Elasticsearch index
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django(object):
        model = Student
        fields = ['id', 'name', 'email', 'city', 'mobile', 'type']
