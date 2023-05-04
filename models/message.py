from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(INTEGER(11), primary_key=True)
    sender_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    recipient_id = Column(ForeignKey('users.id'), index=True)
    group_id = Column(ForeignKey('chat_groups.id'), index=True)
    message_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    group = relationship('ChatGroup')
    recipient = relationship('User', primaryjoin='Message.recipient_id == User.id')
    sender = relationship('User', primaryjoin='Message.sender_id == User.id')
