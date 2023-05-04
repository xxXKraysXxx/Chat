from sqlalchemy import Column, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    last_active_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class ChatGroup(Base):
    __tablename__ = 'chat_groups'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), nullable=False)
    creator_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    creator = relationship('User')


class UserToken(Base):
    __tablename__ = 'user_tokens'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    token = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    expires_at = Column(TIMESTAMP, nullable=False, server_default=text("'0000-00-00 00:00:00'"))

    user = relationship('User')


class ChatGroupMember(Base):
    __tablename__ = 'chat_group_members'

    id = Column(INTEGER(11), primary_key=True)
    group_id = Column(ForeignKey('chat_groups.id'), nullable=False, index=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)

    group = relationship('ChatGroup')
    user = relationship('User')


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


class Attachment(Base):
    __tablename__ = 'attachments'

    id = Column(INTEGER(11), primary_key=True)
    message_id = Column(ForeignKey('messages.id'), nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(255), nullable=False)

    message = relationship('Message')


class UnreadMessage(Base):
    __tablename__ = 'unread_messages'

    id = Column(INTEGER(11), primary_key=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    message_id = Column(ForeignKey('messages.id'), nullable=False, index=True)

    message = relationship('Message')
    user = relationship('User')
