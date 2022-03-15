from django.db import models

from orders.models import Order

# Create your models here.



class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.amount)



class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)


class Product(models.Model):
    product = ProductManager()
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.name