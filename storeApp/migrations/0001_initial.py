# Generated by Django 4.1.7 on 2023-08-20 05:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyStockOrAssets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_number', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_color', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_size', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_image', models.ImageField(upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Company Stock Or Assets',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customer_full_name', models.CharField(max_length=100)),
                ('customer_phone_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of Customers',
            },
        ),
        migrations.CreateModel(
            name='EmergenceInformations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('what_emergence', models.CharField(max_length=2000)),
                ('spending_cost', models.IntegerField()),
                ('spending_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of emergence',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDetailInformations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('employee_Full_name', models.CharField(max_length=200)),
                ('employee_gender', models.CharField(max_length=100)),
                ('employee_email_address', models.EmailField(max_length=254)),
                ('employee_start_date', models.DateField(auto_now_add=True)),
                ('employee_phone_number1', models.CharField(max_length=100)),
                ('employee_phone_number2', models.CharField(max_length=100)),
                ('employee_residence_area', models.CharField(max_length=100)),
                ('employee_username', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_password', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'list of Employees',
            },
        ),
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(blank=True, default='Specify product name', max_length=100, null=True)),
                ('purchase_price', models.CharField(blank=True, default='Specify purchase price', max_length=100, null=True)),
                ('sales_price', models.CharField(blank=True, default='Specify Sales Price', max_length=100, null=True)),
                ('available', models.CharField(blank=True, default='Specify quanity availble', max_length=100, null=True)),
                ('sku_code', models.CharField(blank=True, default='Specify sku or code', max_length=100, null=True)),
                ('unit_code', models.CharField(blank=True, default='specify unit code', max_length=100, null=True)),
                ('bar_code', models.CharField(blank=True, default='Specify bar code', max_length=100, null=True)),
                ('brand', models.CharField(blank=True, default='Specify brand', max_length=100, null=True)),
                ('product_model', models.CharField(blank=True, default='Specify product model', max_length=100, null=True)),
                ('expire_date_in_month_year', models.CharField(blank=True, default='Specify Expire Date', max_length=100, null=True)),
                ('is_raw_material', models.CharField(blank=True, default='Specify is raw material', max_length=100, null=True)),
                ('reorder_level', models.CharField(blank=True, default='Specify reorder level', max_length=100, null=True)),
                ('product_category', models.CharField(blank=True, default='Specify product category', max_length=100, null=True)),
                ('product_description', models.CharField(blank=True, default='Specify product description', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'products List',
            },
        ),
        migrations.CreateModel(
            name='ShopBrandMainLogo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('brand_image', models.ImageField(upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Company logo/  brand',
            },
        ),
        migrations.CreateModel(
            name='ShopsTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_street', models.CharField(max_length=100)),
                ('shop_district', models.CharField(max_length=100)),
                ('shop_region', models.CharField(max_length=100)),
                ('shop_start_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shop_supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.employeedetailinformations')),
            ],
            options={
                'verbose_name_plural': 'Shops List',
            },
        ),
        migrations.CreateModel(
            name='productSoldInCash',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('number_of_product_nedeed', models.IntegerField()),
                ('date_product_sold', models.DateTimeField(auto_now=True)),
                ('total_product_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('store_remain', models.PositiveIntegerField(blank=True, null=True)),
                ('date_for_issues_invoice', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storeApp.customerdetails')),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeApp.producttable')),
                ('shop_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storeApp.shopstable')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'products sold',
            },
        ),
        migrations.CreateModel(
            name='ProductAndSupplierAndReceiverTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_cost', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('product_quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total_product_cost', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('amount_to_sold', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.producttable')),
                ('product_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.employeedetailinformations')),
                ('shop_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeApp.shopstable')),
            ],
            options={
                'verbose_name_plural': 'products received ',
            },
        ),
        migrations.CreateModel(
            name='ManageInvoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('number_of_product_nedeed', models.IntegerField()),
                ('date_product_sold', models.DateTimeField(auto_now=True)),
                ('total_product_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('advance_paid', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('amount_remain_to_be_paid', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('date_for_issues_invoice', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer_full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storeApp.customerdetails')),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeApp.producttable')),
                ('shop_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storeApp.shopstable')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'All Invoices',
            },
        ),
        migrations.CreateModel(
            name='CustomersOrders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customer_order', models.CharField(max_length=2000)),
                ('customer_quantity_nedeed', models.IntegerField()),
                ('delivery_date_expected', models.DateField()),
                ('order_status', models.CharField(default='Pending', max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('custoomer_full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='storeApp.customerdetails')),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'List of Orders from customers',
            },
        ),
        migrations.CreateModel(
            name='AuthorizeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_dashboard', models.BooleanField(default=False)),
                ('manage_employees', models.BooleanField(default=False)),
                ('manage_shop', models.BooleanField(default=False)),
                ('manage_product', models.BooleanField(default=False)),
                ('manage_supplier', models.BooleanField(default=False)),
                ('manage_store', models.BooleanField(default=False)),
                ('manage_sales', models.BooleanField(default=True)),
                ('manage_orders', models.BooleanField(default=True)),
                ('manage_emergence', models.BooleanField(default=True)),
                ('help_center', models.BooleanField(default=True)),
                ('manage_company_stock_or_assets', models.BooleanField(default=False)),
                ('manage_authorizations', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('select_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Authorization',
            },
        ),
    ]
