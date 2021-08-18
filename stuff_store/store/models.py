from django.db import models
from django.urls import reverse
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the full name!")
    stock_count = models.IntegerField(help_text="The current items in the stock")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(verbose_name="stock keeping unit", max_length=20,default="", unique=True)

    class Meta:
        ordering = ['price']
        constraints = [
            models.CheckConstraint(check=models.Q(price_gte=0),name="price_ not_negative")
        ]

    def get_absolute_url(self):
        return reverse("store_product-detail", kwargs={'pk': self.id})

    @property
    def vat(self):
        return Decimal(.3)*self.price

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


    def __str__(self):
        return self.image


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['category_name']


    def __str__(self):
        return self.cat_name



