from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def get_rating(self):
        stars = self.products_stars.all()
        if not stars:
            return 0
        count_stars = len(stars)
        sum_stars = sum(i.rating for i in stars)
        return sum_stars / count_stars

        def __str__(self):
            return f"{self.title}"


from django.db import models

# Create your models here.
