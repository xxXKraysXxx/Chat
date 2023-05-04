from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatGroup(Base):
    __tablename__ = 'chat_groups'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    creator_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    creator = relationship('User')