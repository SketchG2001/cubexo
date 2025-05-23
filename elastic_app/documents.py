from django.core.checks import register
from django_elasticsearch_dsl import Document,Index,fields
from django_elasticsearch_dsl.registries import registry

from .models import ElasticDemo,Car,Product


PUBLISHER_INDEX = Index("elastic_demo")
PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr="id")
    print(id)
    title = fields.TextField(
        fields={
            "raw":{
                "type": "keyword",
            }
        }
    )
    print(title)
    content = fields.TextField(
        fields={
            "raw": {
                "type": "keyword",
            }
        }
    )
    print(content)

    class Django(object):
        model = ElasticDemo



from elasticsearch_dsl import Index as index
from django_elasticsearch_dsl import Document as doc

product = index("product")
product.settings(
    number_of_shards=1,
    number_of_replicas=1
)
@registry.register_document
@product.document
class NewProductDocument(doc):
    class Django:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "category",
        ]











