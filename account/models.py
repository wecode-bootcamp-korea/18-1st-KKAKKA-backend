from django.db import models

from product.models       import Product
from subscription.models  import Subscription

class Account(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50)
    password     = models.CharField(max_length=700)

    class Meta:
        db_table = 'accounts'


class AdditionalInformation(models.Model):
    address      = models.CharField(max_length=100)
    addniversary = models.DateField(auto_now=False, auto_now_add=False)
    account      = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'additional_informations'


class WishList(models.Model):
    account      = models.ForeignKey(Account, on_delete=models.CASCADE)
    product      = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True)
    product_quantity = models.IntegerField()
    subscription = models.ForeignKey(Subscription, models.SET_NULL, blank=True, null=True)
    create_at    = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'WishLists'
