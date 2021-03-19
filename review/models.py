from django.db import models

from account.models      import Account
from lesson.models       import Lesson
from product.models      import Product
from subscription.models import Subscription


class Review(models.Model):
    account      = models.ForeignKey(Account, on_delete=models.CASCADE)
    content      = models.TextField()
    image_url    = models.URLField(max_length=1000)
    rating       = models.IntegerField()
    created_at   = models.DateTimeField(auto_now_add=True)
    product      = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    lesseon      = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        db_table='reviews'
