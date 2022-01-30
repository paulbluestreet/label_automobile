from datetime import datetime
import pytz

from pyramid.view import view_defaults, view_config

from label_automobile.models import Order, OrderProduct, CartProduct


@view_defaults(renderer='json')
class OrderView:
    def __init__(self, request):
        self.request = request
        self.session = request.dbsession

    @view_config(route_name='order.create')
    def order(self):
        user_id = self.request.json_body.get('user_id')
        order_delivery_datetime = self.request.json_body.get('delivery_datetime_UTC')
        order_delivery_datetime = pytz.UTC.localize(datetime.strptime(order_delivery_datetime, '%Y-%m-%d %H:%M:%S'))

        cart_products = self.session.query(CartProduct).filter(CartProduct.user_id == user_id).all()
        if len(cart_products) < 1:
            self.request.response.status = 404
            return "No items in cart"

        order = Order()
        order.user_id = user_id
        order.delivery_datetime = order_delivery_datetime
        self.session.add(order)
        self.session.flush()

        for cart_product in cart_products:
            order_product = OrderProduct()
            order_product.order_id = order.id
            order_product.product_id = cart_product.product_id
            order_product.number = cart_product.number
            self.session.add(order_product)
            self.session.delete(cart_product)

        self.request.response.status = 204
