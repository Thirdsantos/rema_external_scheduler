from datetime import datetime
from sqlalchemy import (
  Column, 
  String, 
  BigInteger,
  TIMESTAMP
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func




class Base(DeclarativeBase):
  pass

class Users(Base):
  __tablename__ = "users"

  id = Column(BigInteger, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  email = Column(String, nullable=False, unique=True)
  created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

class Sections(Base):
  __tablename__ = "section"

  id = Column(BigInteger, primary_key=True, autoincrement=True)
  section_name = Column(String, nullable=False, unique=True)

class SubmissionSchedule(Base):
  __tablename__ = "submission_schedule"

  id = Column(BigInteger, primary_key=True, autoincrement=True)
  created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
  transaction_id = Column(String, nullable=False)
  user_id = Column(BigInteger, nullable=False)
  section_id = Column(BigInteger, nullable =False)
  submission_id = Column(String, nullable=False)

class TransactionSchedule(Base):  # or whatever name you like
    __tablename__ = "transaction_schedule"  # change to your real table name

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )
    created_at = Column(
        TIMESTAMP(timezone=True),   # timestamptz
        server_default=func.now(),
        nullable=False,
    )
    user_id = Column(
        BigInteger,   # int8
        nullable=False,
    )
    transaction_id = Column(
        String,       # varchar
        nullable=False,
    )
    start_time = Column(
        TIMESTAMP(timezone=True),   # timestamptz
        nullable=False,
    )
    end_time = Column(
        TIMESTAMP(timezone=True),   # timestamptz
        nullable=False,
    )
