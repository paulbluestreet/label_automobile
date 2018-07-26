from datetime import datetime
from uuid import uuid4

import pytz
from sqlalchemy import (
    Column,
    DateTime,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.zzzcomputing.com/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)
Base = declarative_base(metadata=metadata)


class BaseModel:
    id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    created = Column(DateTime(timezone=True), default=datetime.now(
        tz=pytz.utc))
    # TODO - default update on persist
    updated = Column(DateTime(timezone=True))