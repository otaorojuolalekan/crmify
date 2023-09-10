from api.database import Base
from sqlalchemy import Column, Integer, String, Enum as SqlEnum, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from enum import Enum

# ENUMERATION CLASSES


class StatusEnum(str, Enum):
    Resolved = "Resolved"
    Unresolved = "Unresolved"


class CategoryEnum(str, Enum):
    Technical = "Technical"
    Commercial = "Commercial"


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    address = Column(String(255))
    email = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=text('now()'))


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, nullable=False)
    # future should be based on preset values....
    category = Column(SqlEnum(CategoryEnum), nullable=False)
    subject = Column(String(100), nullable=False)
    # future should be based on preset values....
    status = Column(SqlEnum(StatusEnum), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    account_id = Column(Integer, ForeignKey(
        "accounts.id", ondelete="CASCADE"), nullable=False)
    account = relationship("Account")
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")


class Update(Base):
    __tablename__ = 'updates'

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    update_text = Column(String(255), nullable=False)
    update_created_by = relationship("User")
    case_id = Column(Integer, ForeignKey(
        "cases.id", ondelete="CASCADE"), nullable=False)
    case_details = relationship("Case")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        server_default=text('now()'))
