from django.db import models

from subscription.models  import Subscription

class Account(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    password     = models.CharField(max_length=300)

    class Meta:
        db_table = 'accounts'


class AdditionalInformation(models.Model):
    address      = models.CharField(max_length=100, blank=True, default='')
    anniversary  = models.DateField(auto_now=False, auto_now_add=False, blank=True, default='')
    account      = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = 'additional_informations'


class WishList(models.Model):
    account          = models.ForeignKey(Account, on_delete=models.CASCADE)
    product          = models.ForeignKey('product.Product', models.SET_NULL, blank=True, null=True)
    product_quantity = models.IntegerField()
    subscription     = models.ForeignKey(Subscription, models.SET_NULL, blank=True, null=True)
    create_at        = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'wishlists'
