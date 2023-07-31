from import_export import resources

from .models import ProductTable


class ProductTableResource(resources.ModelResource):
    class meta:
        model = ProductTable