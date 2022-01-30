from sqlalchemy import Column, String

from label_automobile.models.meta import Base, BaseModel


class Product(BaseModel, Base):
    __tablename__ = 'product'
    name = Column(String, nullable=False)
    details = Column(String, nullable=False)
