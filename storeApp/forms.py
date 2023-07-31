from dataclasses import field, fields
from pyexpat import model
from .models import *
from django.forms import ModelForm
from django import forms 

from django.contrib.auth.forms import UserCreationForm
class ProductTableForm(forms.Form):
  class meta:
    model =ProductTable
    fields = '__all__'
    exclude =[
      'created_at',
      'updated_at'
    ]
# class ProductAndSupplierTableForm(ModelForm):
#   class Meta:
#     model =ProductAndSupplierTable
#     fields = '__all__'
#     exclude =[
#       'created_at',
#       'updated_at'
#     ]
class ProductAndSupplierAndReceiverTableForm(ModelForm):
  class Meta:
    model =ProductAndSupplierAndReceiverTable
    fields = '__all__'
    exclude =[
      'created_at',
      'updated_at'
    ]

class ShopsTableForm(ModelForm):
  class Meta:
    model =ShopsTable
    fields = '__all__'
    exclude =[
      'shop_start_date',
      'created_at',
      'updated_at'
    ]


class EmployeeDetailInformationsForm(ModelForm):
  class Meta:
    model =EmployeeDetailInformations
    fields =  '__all__'
     
    exclude =[
      'employee_start_date',
      'created_at',
      'updated_at'
    ]


class EmployeeAcountForm(UserCreationForm):
  class Meta:
    model =User
    fields =  ['first_name', 'username', 'password1', 'password2']     
   
    #   "employee_Full_name", 
    #  "employee_gender",
    #  "employee_email_address",
    #  "employee_start_date", 
    #  "employee_phone_number1",
    #  "employee_phone_number2", 
    #  "employee_residence_area",
    #  "username",
    #  "password1",
    #  "password2"

# productSoldInCash
class productSoldInCashForm(ModelForm):
  class Meta:
    model = productSoldInCash
    fields = '__all__'
    exclude =[
      'supervisor',
      'date_product_sold',
      'total_product_cost',
      'amount_to_sold',
      'created_at',
      'updated_at'
    ]

# EmergenceInformations
class EmergenceInformationsForm(ModelForm):
  class Meta:
    model = EmergenceInformations
    fields = '__all__'
    exclude =[
      
      'created_at',
      'updated_at'
    ]

# CustomersOrders    
class CustomersOrdersForm(ModelForm):
  class Meta:
    model = CustomersOrders
    fields = '__all__'
    exclude =[
      'supervisor',
      'order_status',
      'created_at',
      'updated_at'
    ]

class AuthorizeUsersForm(ModelForm):
  class Meta:
    model = AuthorizeUsers
    fields ='__all__'
    exclude =[
      
      'created_at',
      'updated_at'
    ]

class CompanyStockOrAssetsForm(ModelForm):
  class Meta:
    model = CompanyStockOrAssets
    fields ='__all__'
    exclude =[
      
      'created_at',
      'updated_at'
    ]
    
    
    
class customerDetailsForm(ModelForm):
  class Meta:
    model = CustomerDetails
    fields ='__all__'
    exclude =[
      
      'created_at',
      'updated_at'
    ]