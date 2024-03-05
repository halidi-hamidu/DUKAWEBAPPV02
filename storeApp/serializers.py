from rest_framework import serializers

from .models import *

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'


    def validate_customer_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Invalid phone number. Must contain only digits.")
        return value

        
    def validate_customer_full_name(self, value):
        if not value.isspace():
            raise serializers.ValidationError("Invalid characters in customer_full_name. Use only spaces.")
        return value

    def validate(self, data):
        return data



class ShopBrandMainLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBrandMainLogo
        fields = '__all__'

class ProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = '__all__'


class EmployeeDetailInformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetailInformations
        fields = '__all__'

class ShopsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopsTable
        fields = '__all__'

class ProductAndSupplierAndReceiverTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAndSupplierAndReceiverTable
        fields = '__all__'


class ProductSoldInCashSerializer(serializers.ModelSerializer):
    class  Meta:
        model = productSoldInCash
        fields = '__all__'

class AuthorizeUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizeUsers
        fields = '__all__'


class CompanyStockOrAssetsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStockOrAssets
        fields  = '__all__'


class ManageInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageInvoice
        fields = '__all__'

class InvoiceNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceNumbers
        fields = '__all__'