from django.db import models

from category.models  import Category


class Subscription(models.Model):
    name         = models.CharField(max_length=50)
    monthly_plan = models.CharField(max_length=50, null = True, default = '')
    price        = models.DecimalField(max_digits=18, decimal_places=2, null = True, default = '')
    # category     = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, default = '')
    introduction = models.CharField(max_length=500, null = True, default = '')

    class Meta:
        db_table = 'subscriptions'


class Detail(models.Model):
    url          = models.URLField(max_length=500)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscription_details'