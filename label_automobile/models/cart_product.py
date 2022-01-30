from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID

from label_automobile.models.meta import Base, BaseModel


class CartProduct(BaseModel, Base):
    __tablename__ = 'cart_product'

    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey('product.id'), nullable=False)
    number = Column(Integer, default=1)

    UniqueConstraint('user_id', 'product_id', name='unique_user_product')
