# Generated by Django 3.1.7 on 2021-03-24 21:08

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
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 21, 8, 36, 15532), null=True, verbose_name='attending_date'),
        ),
        migrations.AlterField(
            model_name='productcart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 21, 8, 36, 14779), null=True, verbose_name='delivery_date'),
        ),
        migrations.AlterField(
            model_name='subscriptioncart',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 24, 21, 8, 36, 15148), null=True, verbose_name='delivery_date'),
        ),
    ]
