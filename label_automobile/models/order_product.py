from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from label_automobile.models.meta import Base, BaseModel


class OrderProduct(BaseModel, Base):
    __tablename__ = 'order_product'
    order_id = Column(UUID(as_uuid=True), ForeignKey('order.id'))
