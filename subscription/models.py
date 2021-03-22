from django.db import models


class Subscription(models.Model):
    name         = models.CharField(max_length=50)
    category     = models.ForeignKey('product.Category', on_delete=models.CASCADE)
    introduction = models.CharField(max_length=500)
    main_image   = models.URLField(max_length=500)

    class Meta:
        db_table = 'subscriptions'


class SubscriptionDetail(models.Model):
    url          = models.URLField(max_length=500)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscription_details'


class MonthlyPlan(models.Model):
    name = models.CharField(max_length=100)
    subscription = models.ManyToManyField(
        Subscription,
        through = 'SubscriptionPlan'
    )

    class Meta:
        db_table = 'monthly_plans'


class SubscriptionPlan(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    monthly_plan = models.ForeignKey(MonthlyPlan, on_delete=models.CASCADE)
    price        = models.DecimalField(max_digits=18, decimal_places=0)

    class Meta:
        db_table = 'subscription_plan'