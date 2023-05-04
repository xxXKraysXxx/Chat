from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UnreadMessage(Base):
    __tablename__ = 'unread_messages'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    message_id = Column(ForeignKey('messages.id'), nullable=False, index=True)

    message = relationship('Message')
    user = relationship('User')
