import pytz
from datetime import datetime

from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from label_automobile.models.meta import Base, BaseModel


class Order(BaseModel, Base):
    __tablename__ = 'order'
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    delivery_datetime = Column(DateTime(timezone=True), default=datetime.now(tz=pytz.utc))
