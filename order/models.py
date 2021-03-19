import datetime

from django.db    import models
from django.utils import timezone

from account.models      import Account
from lesson.models       import LessonLocation
from product.models      import Product, OptionProduct, OptionSubscription
from subscription.models import SubscriptionPlan



class Address(models.Model):
    sender                 = models.CharField(max_length=50, null=True, blank=True)
    recipient              = models.CharField(max_length=100)
    recipient_phone_number = models.CharField(max_length=100)
    postal_code            = models.IntegerField() 
    address                = models.CharField(max_length=200)
    save_option            = models.BooleanField()

    class Meta:
        db_table = 'addresses'
    

class Status(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'status'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'payment_methods'


class Order(models.Model):
    account       = models.ForeignKey(Account, on_delete=models.CASCADE)
    address       = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True)
    paymentmethod = models.ForeignKey(PaymentMethod, models.SET_NULL, blank=True, null=True)
    status        = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    product       = models.ManyToManyField(
        Product,
        through = 'ProductCart',
    )
    product_option = models.ManyToManyField(
        OptionProduct,
        through = 'ProductCart',
    )
    subscriptionplan  = models.ManyToManyField(
        SubscriptionPlan,
        through = 'SubscriptionCart'
    )
    subscription_option = models.ManyToManyField(
        OptionSubscription,
        through = 'SubscriptionCart'
    )
    lesson_location = models.ManyToManyField(
        LessonLocation,
        through = 'LessonCart'
    )

    class Meta:
        db_table = 'orders'


class ProductCart(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    product         = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_product  = models.ForeignKey(OptionProduct, on_delete=models.CASCADE)
    quantity        = models.IntegerField(default=1, blank=True, null=False)
    delivery_date   = models.DateField (('delivery_date'), default=timezone.now(), null=True)
    
    class Meta:
        db_table = 'product_carts'


class SubscriptionCart(models.Model):
    order                = models.ForeignKey(Order, on_delete=models.CASCADE)
    subscription         = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    subscription_option  = models.ForeignKey(OptionSubscription, on_delete=models.CASCADE)
    quantity             = models.IntegerField(default=1, blank=True, null=False)
    delivery_date        = models.DateField (('delivery_date'), default=timezone.now(), null=True)

    class Meta:
        db_table = 'subscriptions_carts'


class LessonCart(models.Model):
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    lesson_location = models.ForeignKey(LessonLocation, on_delete=models.CASCADE)
    attending_date  = models.DateField(('attending_date'), default=timezone.now(), null=True)

    class Meta:
        db_table = 'lesson_carts'