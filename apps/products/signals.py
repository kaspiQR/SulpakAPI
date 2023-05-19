from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import Product


@receiver(post_save, sender=Product)
def create(sender, instance, created, **kwargs):
    if created:
        print("Successfully created: ", instance.title)

