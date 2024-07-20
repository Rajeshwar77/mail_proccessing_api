import datetime

from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    token = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())


class Email(Base):
    __tablename__ = "emails"
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    message_id = Column(String, primary_key=True, index=True)
    sender = Column(String, index=True)
    receiver = Column(String, index=True)
    subject = Column(String, index=True)
    message = Column(Text)
    received_at = Column(DateTime, index=True)
    history_id = Column(String)
    is_read = Column(Boolean, default=False)
    folder = Column(String, default="inbox")

# Email needs table needs to be partitioned by user_id and received_at

