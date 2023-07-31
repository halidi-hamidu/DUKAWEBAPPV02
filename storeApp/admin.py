from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(ProductTable)
# admin.site.register(ProductAndSupplierTable)
admin.site.register(ProductAndSupplierAndReceiverTable)
admin.site.register(ShopsTable)
admin.site.register(EmployeeDetailInformations)
admin.site.register(productSoldInCash)
admin.site.register(EmergenceInformations)
admin.site.register(CustomersOrders)
admin.site.register(AuthorizeUsers)
admin.site.register(CompanyStockOrAssets)
admin.site.register(ShopBrandMainLogo)
admin.site.register(CustomerDetails)