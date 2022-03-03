import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from buyers.models import Buyers
from .models import Cars

@receiver(pre_save, sender=Cars)
def post_modify_and_create_code(sender, instance, **kwargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    obj = Buyers.objects.get(user=instance.buyer.user)
    obj.from_signal = True
    obj.save()    

