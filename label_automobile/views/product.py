from pyramid.view import view_defaults, view_config

from label_automobile.models import Product


@view_defaults(renderer='json')
class ProductView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession
        self.product_id = request.matchdict.get('product_id', None)

    @view_config(route_name='product.list')
    def list(self):
        return [{
            "name": product.name,
            "id": str(product.id)
        } for product in self.session.query(Product).all()]

    @view_config(route_name='product.details')
    def details(self):
        product = self.session.query(Product).get(self.product_id)
        return {"id": product.id,
                "name": product.name,
                "details": product.details}
