from django.db import models



class ElasticDemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Car(models.Model):

    TYPE_CHOICES = (
    (1,1),
    (2,2),
    (3,3),
    )

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.IntegerField(choices=TYPE_CHOICES)

    def type_to_string(self):
        if self.type == 1:
            return 'Ford'
        elif self.type == 2:
            return 'BMW'
        else:
            return 'Mercedes'

    def __str__(self):
        return self.name + ' ' + self.type_to_string()


class Product(models.Model):

    CATEGORY_CHOICES = (
    ('Beauty','Beauty'),
    ('Home','Home'),
    ('Sanitation','Sanitation'),
    ('daily needs','Daily needs'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)

    def __str__(self):
        return self.name