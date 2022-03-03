from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Buyers


@receiver(post_save, sender=User)
def post_save_create_buyers(sender, instance, created, **kwargs):
    print("sender", sender)
    print("instant", instance)
    print('created', created)
    print('kwargs', kwargs)
    if created:
        Buyers.objects.create(user=instance)