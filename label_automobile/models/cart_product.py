from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from label_automobile.models.meta import Base, BaseModel


class CartProduct(BaseModel, Base):
    __tablename__ = 'cart_product'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    product_id = Column(UUID(as_uuid=True), ForeignKey('product.id'))
