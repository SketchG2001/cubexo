from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator



class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2,max_digits=10)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " "+ self.email
    


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length=100)
    address = models.TextField()
    res_type = models.CharField(max_length=3,choices=TypeChoices)

    def __str__(self):
        return self.name
    



class Ratings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return f"Rating: {self.rating}"
    

class Sales(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,on_delete=models.CASCADE,null=True,related_name='sales'
    )
    income = models.DecimalField(max_digits=8,decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self):
        return str(self.income)

