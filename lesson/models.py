from django.db import models

from product.models import Category


class Lesson(models.Model):
    introduction = models.CharField(max_length=50)
    name         = models.CharField(max_length=50)
    category     = models.ForeignKey('product.Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lessons'


class Location(models.Model):
    name          = models.CharField(max_length=100)
    desctiption   = models.CharField(max_length=500)
    lesson        = models.ManyToManyField(
        Lesson,
        through        = 'LessonLocation',
        through_fields = ('location', 'lesson'),
    )

    class Meta:
        db_table = 'locations'


class LessonLocation(models.Model):
    location         = models.ForeignKey(Location, on_delete=models.CASCADE)
    lesson           = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    price            = models.DecimalField(max_digits=10, decimal_places=2)
    discount_rate    = models.FloatField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'lesson_locations'