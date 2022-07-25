from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from marketplace.settings import AUTH_USER_MODEL

"""
Product
- Nom (char)
- Prix (float / integer)
- Stock (integer)
- Description (text)
- Image (image)
- Slug (slug)

"""


class Product(models.Model):
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


"""
Commande (Order)
- Utilisateur (CustomUser)
- Produit (Product)
- Quantité (Integer)
- Commandé ou non (boolean)
- Date de la commande
"""


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


"""
Panier (Cart)
- Utilisateur (CustomUser)
- Articles (Order)
"""


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.user_name

    def order(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.orders.all().delete()
        super().delete(*args, **kwargs)