# Generated by Django 4.1.7 on 2023-08-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(blank=True, default='MAG0001', max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Invoices Numbers ',
            },
        ),
    ]