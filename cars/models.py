from django.db import models
from  buyers.models import Buyers
import uuid

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = str(uuid.uuid4()).replace('-','').upper()[:10]
            return super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyer}"


    