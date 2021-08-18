from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the full name!")
    stock_count = models.IntegerField(help_text="The current items in the stock")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(default="", blank=True)
    sku = models.CharField(verbose_name="stock keeping unit", max_length=20,default="", unique=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


    def __str__(self):
        return self.image


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.cat_name



