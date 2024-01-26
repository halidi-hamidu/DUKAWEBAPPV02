from django.urls import path, include
from . import views

from .views import CustomerDetailsListCreateView
from .views import ShopBrandMainLogoListView
from .views import ProductTableListView
from .views import EmployeeDetailInformationsListView
from .views import ShopsTableListView
from .views import ProductAndSupplierAndReceiverTableListView
from .views import ProductSoldInCashSerializerListView
# from .views import GeneratePdf

app_name = 'storeApp'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('homepage', views.homepage, name="homepage"),
    path('logout-user', views.logoutPage, name="logoutPage"),
    path('storePage', views.storePage, name="storePage"),
    path('my-shops', views.shopPage, name="shopPage"),
    # path('my-suppliers', views.suppliersPage, name="suppliersPage"),
    path('my-employees', views.employeePage, name="employeePage"),
    path('my-sales', views.salesPage, name="salesPage"),
    path('my-products', views.productPage, name="productPage"),
    path('import-excel-file', views.importExcelFile, name="importExcelFile"),
    path('my-orders', views.ordersPage, name="ordersPage"),
    path('my-emergence', views.emergencePage, name="emergencePage"),
    path('users-authorization', views.authorizationPage, name="authorizationPage"),
    path('change-order-status/<str:id>/', views.changeOrderStatus, name="changeOrderStatus"),
    path('update-order/<str:id>/', views.updateOrder, name="updateOrder"),
    path('delete-order/<str:id>/', views.deleteOrder, name="deleteOrder"),
    path('update-emergence/<str:id>/', views.updateEmergence, name="updateEmergence"),
    path('delete-emergence/<str:id>/', views.deleteEmergence, name="deleteEmergence"),
    path('update-user-auth/<str:id>/', views.updateUserAuthorizations, name="updateUserAuthorizations"),
    path('delete-user-auth/<str:id>/', views.deleteUserAuthorizations, name="deleteUserAuthorizations"),
    path('delete/<str:id>/', views.deleteUser, name="deleteUser"),
    path('delete-shop/<str:id>/', views.deleteShop, name="deleteShop"),
    path('delete-product/<str:id>/', views.deleteProduct, name="deleteProduct"),
    path('delete-supplier/<str:id>/', views.deleteSupplier, name="deleteSupplier"),
    path('delete-product-sold/<str:id>/', views.deleteProductSold, name="deleteProductSold"),
    path('delete-product-in-store/<str:id>/', views.deleteProductInStore, name="deleteProductInStore"),
    path('activate-user/<str:id>/', views.activateUserAuthorizations, name="activateUserAuthorizations"),
    path('deactivate-user/<str:id>/', views.deactivateUserAuthorizations, name="deactivateUserAuthorizations"),
    path('pdf/<str:id>/', views.generatePdf, name ="generatePdf"),
    path('print-profoma-pdf/<str:id>/', views.generatePdfForInvoice, name ="generatePdfForInvoice"),
    path('company-Stock', views.companyStockPage, name="companyStockPage"),
    path('customer-details', views.customerDetails, name="customerDetails"),
    path('manage-invoices', views.manageInvoice, name="manageInvoice"),
    path('manage-profoma-invoice', views.profomaInvoice, name="profomaInvoice"),
    path('cancel-profoma-invoice/<str:id>/', views.cancelProfomaInvoice, name="cancelProfomaInvoice"),
    path('cancelled-profoma-invoice', views.cancelledInvoice, name="cancelledInvoice"),
    path('add-amount-to-pay-invoice/<str:id>/', views.addAmountToItemFromInvoice, name="addAmountToItemFromInvoice"),
    path('partial-paid-invoices', views.partialPaidInvoices, name="partialPaidInvoices"),
    path('full-paid-invoices', views.fullPaidinvoices, name="fullPaidinvoices"),
    path('all-invoices', views.allInvoicesList, name='allInvoicesList'),

    # api urls hizi ndo endpoint zanguu baadhii
    path('api/customers-details/', CustomerDetailsListCreateView.as_view(), name='customer-details-list-create'),
    path('api/shops-logo/', ShopBrandMainLogoListView.as_view(), name='shopLogo'),
    path('api/products-list', ProductTableListView.as_view(), name='productList'),
    path('api/employee-list/', EmployeeDetailInformationsListView.as_view(), name='employee-list'),
    path('api/shops-list/', ShopsTableListView.as_view(), name='shopsList'),
    path('api/products-recived-store-direct/', ProductAndSupplierAndReceiverTableListView.as_view(), name='productAndSupplierAndReceiver'),
    path('api/product-solid-in-cash', ProductSoldInCashSerializerListView.as_view(), name='productSolidIncash')


    
]
