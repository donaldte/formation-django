from django.db.models.signals import pre_delete
from django.dispatch import receiver
from sale.models import Sale


@receiver(pre_delete, sender=Sale)
def pre_delete_chance_active_order(sender, instance, **kwargs):
    obj = instance.order
    obj.activate = False
    obj.save()
