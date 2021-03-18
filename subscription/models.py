from django.db import models

from category.models  import Category


class Subscription(models.Model):
    name         = models.CharField(max_length=50)
    monthly_plan = models.CharField(max_length=50)
    price        = models.DecimalField(max_digits=18, decimal_places=2)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=500)

    class Meta:
        db_table = 'subscriptions'


class SubscriptionDetail(models.Model):
    url          = models.URLField(max_length=500)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscription_details'