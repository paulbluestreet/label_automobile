def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('user.list', '/user', request_method="GET")
    config.add_route('user.find_by_email', '/user/email', request_method="GET")
