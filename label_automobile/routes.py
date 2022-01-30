def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('user.list', '/user', request_method="GET")
    config.add_route('user.find_by_email', '/user/email', request_method="GET")

    # Product routers
    config.add_route('product.list', '/product', request_method='GET')
    config.add_route('product.details', '/product/{product_id}', request_method='GET')

    # Shopping cart routes
    config.add_route('cart_product.list', '/cart_product', request_method="GET")
    config.add_route('cart_product.add', '/cart_product', request_method="POST")
    config.add_route('cart_product.delete', '/cart_product', request_method="DELETE")

    # order routers
    config.add_route('order.create', '/order', request_method="POST")