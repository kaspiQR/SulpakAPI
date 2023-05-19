from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..customers.models import CustomUser
from apps.products.models import Product


class Comment(models.Model):
    text = models.CharField(max_length=150, blank=True, null=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_comments')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"


class Stars(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_stars')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}"


from django.db import models

# Create your models here.
