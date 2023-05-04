from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserToken(Base):
    __tablename__ = 'user_tokens'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    token = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    expires_at = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))

    user = relationship('User')