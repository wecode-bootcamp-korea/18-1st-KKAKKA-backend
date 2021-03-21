# Generated by Django 3.1.7 on 2021-03-21 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'monthly_plans',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
                ('main_image', models.URLField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=18)),
                ('monthly_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.monthlyplan')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.subscription')),
            ],
            options={
                'db_table': 'subscription_plan',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=500)),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscription.subscription')),
            ],
            options={
                'db_table': 'subscription_details',
            },
        ),
        migrations.AddField(
            model_name='monthlyplan',
            name='subscription',
            field=models.ManyToManyField(through='subscription.SubscriptionPlan', to='subscription.Subscription'),
        ),
    ]
