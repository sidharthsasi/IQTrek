from django.db import models

# Create your models here.


class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField()
    table_booking = models.BooleanField(default=False)
    online_delivery = models.BooleanField(default=False)
    cuisines = models.ManyToManyField(Cuisine)
    country_code = models.CharField(max_length=10)
    city_code = models.CharField(max_length=10)
    Cuisines = models.ForeignKey(Cuisine,on_delete=models.CASCADE,related_name='restaurants')

    def __str__(self):
        return self.name