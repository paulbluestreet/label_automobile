from pyramid.view import view_defaults, view_config
from sqlalchemy.orm.exc import NoResultFound

from label_automobile.models import CartProduct, Product


@view_defaults(renderer='json')
class CartProductView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='cart_product.list')
    def list(self):
        user_id = self.request.params.get('user_id', None)
        q = self.session.query(CartProduct.number,
                               Product.name,
                               Product.id.label('product_id')).join(Product)
        q = q.filter(CartProduct.user_id == user_id)
        return [{
            "product_name": cart_product.name,
            "number": cart_product.number,
            "product_id": str(cart_product.product_id)
        } for cart_product in q.all()]

    @view_config(route_name='cart_product.add')
    def add(self):
        user_id = self.request.json_body.get('user_id')
        product_id = self.request.json_body.get('product_id')

        try:
            cart_product = self.session.query(CartProduct).filter(CartProduct.user_id == user_id,
                                                                  CartProduct.product_id == product_id).one()
            cart_product.number += 1
        except NoResultFound:
            cart_product = CartProduct()
            cart_product.user_id = user_id
            cart_product.product_id = product_id
        self.session.add(cart_product)

        self.request.response.status = 204

    @view_config(route_name='cart_product.delete')
    def delete(self):
        user_id = self.request.json_body.get('user_id')
        product_id = self.request.json_body.get('product_id')

        try:
            cart_product = self.session.query(CartProduct).filter(CartProduct.user_id == user_id,
                                                                  CartProduct.product_id == product_id).one()
            if cart_product.number > 1:
                cart_product.number -= 1
            else:
                self.session.delete(cart_product)
            self.request.response.status = 204

        except NoResultFound:
            self.request.response.status = 404
            return "Product not in cart"

