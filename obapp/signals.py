
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Restaurant,Ratings,Sales
import datetime
from .views import send_mes


@receiver(post_save,sender=Restaurant)
def create_rat_sal(sender,instance,created,**kwargs):
    if created:
        Sales.objects.create(restaurant=instance,income=500,datetime=datetime.datetime.now())



@receiver(post_delete,sender=Restaurant)
def send_delete_email(sender,instance,**kwargs):
    print(instance.id)
    print(instance.address)
    print(instance.res_type)
    email = "vikasgole089@gmail.com"
    send_mes(email=email)
    