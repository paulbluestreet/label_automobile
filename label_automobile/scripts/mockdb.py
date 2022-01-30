import os
import sys
import transaction as ts

from sqlalchemy.orm.exc import NoResultFound

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_tm_session,
    get_session_factory,
    User,
    Product,
    CartProduct,
    Order,
    OrderProduct
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)
    session_factory = get_session_factory(engine)

    with ts.manager:
        dbsession = get_tm_session(session_factory, ts.manager)

        # Delete all current mockdata
        for table in [CartProduct, OrderProduct, User, Product, Order]:
            dbsession.query(table).delete()
        dbsession.flush()

        user = User()
        user.name = "John"
        user.surname = "Doe"
        user.email = "johndoe@example.com"
        dbsession.add(user)

        for product_example in [('Awesome Car Part', 'This product makes your care even more awesome'),
                                ('Crappy Car Part', 'This product makes your brakes stop working')]:
            product = Product()
            product.name = product_example[0]
            product.details = product_example[1]
            dbsession.add(product)
            dbsession.flush()

        cart_product = CartProduct()
        cart_product.user_id = user.id
        cart_product.product_id = product.id
        dbsession.add(cart_product)
