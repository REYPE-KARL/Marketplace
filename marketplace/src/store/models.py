from django.db import models

# Create your models here.
from django.urls import reverse

"""
Product
- Nom (char)
- Prix (float / integer)
- Stock (integer)
- Description (text)
- Image (image)
- Slug (slug)

"""

class Product (models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})