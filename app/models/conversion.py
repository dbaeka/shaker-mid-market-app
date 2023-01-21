from sqlalchemy import Column, ForeignKey, Integer, JSON, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class Conversion(Base):
    id = Column(Integer, primary_key=True, index=True)
    value = Column(JSON, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="conversions")
