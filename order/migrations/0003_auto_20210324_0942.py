# Generated by Django 3.1.7 on 2021-03-24 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210324_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessoncart',
            name='attending_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 9, 42, 31, 520010), null=True, verbose_name='attending_date'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 9, 42, 31, 519229), null=True, verbose_name='delivery_date'),
        ),
        migrations.AlterField(
            model_name='subscriptioncart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 9, 42, 31, 519719), null=True, verbose_name='delivery_date'),
        ),
    ]
