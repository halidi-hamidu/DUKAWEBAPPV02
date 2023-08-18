from datetime import date
from itertools import product
from django.db import models
import uuid
from django.contrib.auth.models import User
# from twilio.rest import Client
import os
from  django.utils.timezone import now
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class CustomerDetails(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_full_name = models.CharField(max_length=100)
    customer_phone_number = models.IntegerField()
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of Customers'

    def __str__(self):
        return str(self.customer_full_name)
    
    
class ShopBrandMainLogo(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    brand_image = models.ImageField(upload_to='media')
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Company logo/  brand'

    def __str__(self):
        return str(self.id)

class ProductTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=100, default="Specify product name", blank = True, null=True)
    purchase_price = models.CharField(max_length = 100, default="Specify purchase price", blank = True, null=True)
    sales_price = models.CharField(max_length = 100, default = "Specify Sales Price", blank = True, null=True) 
    available = models.CharField(max_length = 100, default="Specify quanity availble", blank = True, null=True)
    sku_code = models.CharField(max_length = 100, default="Specify sku or code", blank = True, null=True)
    unit_code = models.CharField(max_length = 100, default = "specify unit code", blank = True, null=True)
    bar_code = models.CharField(max_length = 100, default = "Specify bar code", blank = True, null=True)
    brand = models.CharField(max_length = 100, default="Specify brand", blank = True, null=True)
    product_model = models.CharField(max_length = 100, default ="Specify product model", blank = True, null=True )
    expire_date_in_month_year = models.CharField(max_length = 100, default = "Specify Expire Date", blank = True, null=True)
    is_raw_material = models.CharField(max_length = 100, default= "Specify is raw material", blank = True, null=True)
    reorder_level = models.CharField(max_length = 100, default = "Specify reorder level", blank = True, null=True)
    product_category = models.CharField(max_length = 100, default = "Specify product category", blank = True, null=True)
    product_description = models.CharField(max_length = 100, default = "Specify product description", blank = True, null=True)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products List'

    def __str__(self):
        return str(self.product_name)


# class ProductAndSupplierTable(models.Model):
#     id = models.UUIDField(
#         primary_key=True, default=uuid.uuid4, editable=False, unique=True)
#     supplier_full_name = models.CharField(max_length=100)
#     supplier_phone_number = models.CharField(max_length=100)
#     gender = models.CharField(max_length=100)
#     product_name = models.ManyToManyField(ProductTable)
#     # never change once the object is created
#     created_at = models.DateTimeField(auto_now_add=True)
#     # always change when object is updated
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name_plural = 'suppliers products List'

#     def __str__(self):
#         return str(self.supplier_full_name)


# EmployeeDetailInformations
class EmployeeDetailInformations(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    employee_Full_name = models.CharField(max_length=200)
    employee_gender = models.CharField(max_length=100)
    employee_email_address = models.EmailField()
    employee_start_date = models.DateField(auto_now_add=True)
    employee_phone_number1 = models.CharField(max_length=100)
    employee_phone_number2 = models.CharField(max_length=100)
    employee_residence_area = models.CharField(max_length=100)
    employee_username = models.CharField(max_length=100, null=True, blank=True)
    employee_password = models.CharField(max_length=100, null=True, blank=True)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'list of Employees'

    def __str__(self):
        return str(self.employee_Full_name)

# ShopsTable


class ShopsTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    shop_name = models.CharField(max_length=100)
    shop_street = models.CharField(max_length=100)
    shop_district = models.CharField(max_length=100)
    shop_region = models.CharField(max_length=100)
    shop_start_date = models.DateTimeField(auto_now_add=True)
    shop_supervisor = models.ForeignKey(
        EmployeeDetailInformations, on_delete=models.CASCADE)
#   created_at = models.DateTimeField(auto_now_add =True) #never change once the object is created
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Shops List'

    def __str__(self):
        return str(self.shop_name)

# ProductAndSupplierAndReceiverTable


class ProductAndSupplierAndReceiverTable(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.ForeignKey(ProductTable, on_delete=models.CASCADE)
    product_cost = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    product_quantity = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    total_product_cost = models.PositiveIntegerField(
        null=True, blank=True, default=0)
    amount_to_sold = models.PositiveIntegerField(null=True, blank=True)
  
    shop_info = models.ForeignKey(ShopsTable, on_delete=models.CASCADE)
    product_receiver = models.ForeignKey(
        EmployeeDetailInformations, on_delete=models.CASCADE)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products received '

    def __str__(self):
        return str(self.product_name)

# productSoldInCash

# 
class productSoldInCash(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    product_name = models.ForeignKey(
        ProductTable, on_delete=models.SET_NULL, null=True)
    customer_full_name = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, blank=True, null=True)
    number_of_product_nedeed = models.IntegerField()
    date_product_sold = models.DateTimeField(auto_now=True)
    total_product_cost = models.PositiveIntegerField(null=True, blank=True)
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    shop_name = models.ForeignKey(ShopsTable, on_delete=models.CASCADE, null=True, blank=True)
    store_remain = models.PositiveIntegerField(null=True, blank=True)
    
    date_for_issues_invoice = models.DateField(("Date"), default=date.today)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products sold'

    def __str__(self):
        return str(self.product_name)
    
class ManageInvoice(models.Model):
    INVOICE_TYPE = (
        ('', 'Select type of Invoices'),
        ('profoma', 'Profoma'),
        ('unPaidInvoice', 'unPaidInvoice'),
        ('paidInvoice', 'paidInvoice'),
        ('cancelledInvoice', 'cancelledInvoice'),
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_full_name = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.ForeignKey(
        ProductTable, on_delete=models.SET_NULL, null=True)
    number_of_product_nedeed = models.IntegerField()
    date_product_sold = models.DateTimeField(auto_now=True)
    total_product_cost = models.PositiveIntegerField(null=True, blank=True)
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    shop_name = models.ForeignKey(ShopsTable, on_delete=models.CASCADE, null=True, blank=True)
    invoice_type = models.CharField(max_length= 100, choices = INVOICE_TYPE,null=True, blank=True)
    
    date_for_issues_invoice = models.DateField(("Date"), default=date.today)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'All Invoices'

    def __str__(self):
        return str(self.product_name) 


# EmergenceInformations
class EmergenceInformations(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    what_emergence = models.CharField(max_length=2000)
    spending_cost = models.IntegerField()
    spending_date = models.DateField()
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of emergence'

    def __str__(self):
        return str(self.what_emergence)


class CustomersOrders(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    custoomer_full_name = models.ForeignKey(CustomerDetails, on_delete=models.SET_NULL, null=True, blank=True)
    customer_order = models.CharField(max_length=2000)
    customer_quantity_nedeed = models.IntegerField()
    delivery_date_expected = models.DateField()
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_status = models.CharField(max_length=300, default="Pending")
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'List of Orders from customers'

    def __str__(self):
        return str(self.customer_Full_name)


class AuthorizeUsers(models.Model):
    select_user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_dashboard = models.BooleanField(default=False)
    manage_employees = models.BooleanField(default=False)
    manage_shop = models.BooleanField(default=False)
    manage_product = models.BooleanField(default=False)
    manage_supplier = models.BooleanField(default=False)
    manage_store = models.BooleanField(default=False)
    manage_sales = models.BooleanField(default=True)
    manage_orders = models.BooleanField(default=True)
    manage_emergence = models.BooleanField(default=True)
    help_center = models.BooleanField(default=True)
    manage_company_stock_or_assets = models.BooleanField(default=False)
    manage_authorizations = models.BooleanField(default=False)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Authorization'

    def __str__(self):
        return str(self.select_user)

# CompanyStockOrAssets


class CompanyStockOrAssets(models.Model):
    stock_name = models.CharField(max_length=100, blank=True, null=True)
    stock_number = models.CharField(max_length=100, blank=True, null=True)
    stock_color = models.CharField(max_length=100, null=True, blank=True)
    stock_size = models.CharField(max_length=100, null=True, blank=True)
    stock_image = models.ImageField(upload_to='media')
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Company Stock Or Assets'

    def __str__(self):
        return str(self.stock_name)

class ManageInvoice(models.Model):
    INVOICE_TYPE = (
        ('', 'Select type of Invoices'),
        ('profoma', 'Profoma'),
        ('unPaidInvoice', 'unPaidInvoice'),
        ('paidInvoice', 'paidInvoice'),
        ('cancelledInvoice', 'cancelledInvoice'),
    )
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_full_name = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.ForeignKey(
        ProductTable, on_delete=models.SET_NULL, null=True)
    number_of_product_nedeed = models.IntegerField()
    date_product_sold = models.DateTimeField(auto_now=True)
    total_product_cost = models.PositiveIntegerField(null=True, blank=True)
    advance_paid = models.PositiveIntegerField( default=0, null=True, blank=True)
    amount_remain_to_be_paid = models.PositiveIntegerField( default=0, null=True, blank=True)
    supervisor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    shop_name = models.ForeignKey(ShopsTable, on_delete=models.CASCADE, null=True, blank=True)
    
    
    date_for_issues_invoice = models.DateField(("Date"), default=date.today)
    # never change once the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # always change when object is updated
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'All Invoices'

    def __str__(self):
        return str(self.product_name) 