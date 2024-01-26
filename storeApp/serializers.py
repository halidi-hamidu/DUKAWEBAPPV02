from rest_framework import serializers

from .models import *

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'



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