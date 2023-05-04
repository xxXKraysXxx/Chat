from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Attachment(Base):
    __tablename__ = 'attachments'

    id = Column(INTEGER(11), primary_key=True)
    message_id = Column(ForeignKey('messages.id'), nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(255), nullable=False)

    message = relationship('Message')