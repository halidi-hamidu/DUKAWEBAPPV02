# Generated by Django 4.1.7 on 2023-08-22 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0006_manageinvoice_total_profit_obtained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manageinvoice',
            name='total_profit_obtained',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
