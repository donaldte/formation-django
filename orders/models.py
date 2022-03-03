from cars.models import Cars
from django.db import models
# Create your models here.




class Order(models.Model):
    name = models.CharField(max_length=100)
    cars = models.ManyToManyField(Cars)
    total = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.name
