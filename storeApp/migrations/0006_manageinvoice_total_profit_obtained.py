# Generated by Django 4.1.7 on 2023-08-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0005_productsoldincash_total_profit_obtained'),
    ]

    operations = [
        migrations.AddField(
            model_name='manageinvoice',
            name='total_profit_obtained',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]