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


class Option(models.Model):
    name         = models.CharField(max_length=100)
    price        = models.DecimalField(max_digits=18, decimal_places=0)
    product      = models.ManyToManyField(
        Product,
        through        ='OptionProduct',
        through_fields = ('option','product')
        )
    subscription = models.ManyToManyField(
        Subscription,
        through        = 'OptionSubscription',
        through_fields = ('option', 'subscription')
        )
    
    class Meta:
        db_table = 'options'


class OptionProduct(models.Model):
    option  = models.ForeignKey(Option, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table ='option_products'


class OptionSubscription(models.Model):
    option       = models.ForeignKey(Option, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table = 'option_subscriptions'