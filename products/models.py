from tabnanny import verbose
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(null=True)
    actif = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural =("Products")

    def __str__(self):
        return self.name    