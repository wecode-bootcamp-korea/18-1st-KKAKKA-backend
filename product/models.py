from django.db       import models


from category.models     import Category
from subscription.models import Subscription


class Product(models.Model):
    category         = models.ForeignKey(Category, on_delete=models.CASCADE)
    name             = models.CharField(max_length=100)
    introduction     = models.CharField(max_length=500)
    orign_price      = models.DecimalField(max_digits=18, decimal_places=0)
    discount_rate    = models.FloatField()
    discounted_price = models.DecimalField(max_digits=18, decimal_places=0)
    created_at       = models.DateField(auto_now_add=True)
    updated_at       = models.DateField(auto_now=True)

    class Meta:
        db_table = 'products'

class ProductSize(models.Model):
    name    = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'productsizes'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url     = models.URLField(max_length=500)

    class Meta:
        db_table = 'productimages'


class option(models.Model):
    name         = models.CharField(max_length=100)
    price        = models.DecimalField(max_digits=18, decimal_places=0)
    product      = models.ManyToManyField(Product)
    subscription = models.ManyToManyField(Subscription)

    class Meta:
        db_table = 'options'