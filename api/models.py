from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Product(models.Model):
    sku = models.CharField(default=0, max_length=255, unique=True, blank=False,
        primary_key=True)
    name = models.CharField(default="Product Name", max_length=255, blank=False)
    quantity = models.IntegerField(default=1, validators = [MinValueValidator(0)])
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2,
        validators = [MinValueValidator(0.00)])

def __str__(self):
    return self.title
