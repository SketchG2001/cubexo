from django.db import models


class Student(models.Model):
    TYPE_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)

    def number_to_type(self):
        if self.type == 1:
            return 'CSE'
        elif self.type == 2:
            return 'IT'
        elif self.type == 3:
            return 'ME'
        elif self.type == 4:
            return 'CE'
        elif self.type == 5:
            return 'EE'
        else:
            return 'Unknown'

    def __str__(self):
        return self.name
