from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ChatGroupMember(Base):
    __tablename__ = 'chat_group_members'

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(ForeignKey('chat_groups.id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)

    group = relationship('ChatGroup')
    user = relationship('User')
