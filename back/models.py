from database import Base
from sqlalchemy import Integer, String, Column, Boolean, ForeignKey, Float, DATE, DateTime, Interval
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "app_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    failed_logins = Column(Integer, default=0)
    locked_until = Column(DateTime, default=None)
    wallets = relationship("Wallet", back_populates="user")
    access_token = Column(String)
    restore_token = Column(String, default=None)


class Wallet(Base):
    __tablename__ = "app_wallets"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float)
    currency = Column(String, default="USD")
    user_id = Column(Integer, ForeignKey("app_users.id"))
    user = relationship("User", back_populates="wallets")
    incomes = relationship("Income", back_populates="wallet")
    expenses = relationship("Expense", back_populates="wallet")


class Transaction(Base):
    __tablename__ = "app_transactions"

    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, ForeignKey("app_wallets.id"))
    amount = Column(Float)
    type = Column(String)

class Income(Base):
    __tablename__ = "app_incomes"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    wallet_id = Column(Integer, ForeignKey("app_wallets.id"))
    amount = Column(Float)
    category = Column(String)
    wallet = relationship("Wallet", back_populates="incomes")
    

class Expense(Base):
    __tablename__ = "app_expenses"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    wallet_id = Column(Integer, ForeignKey("app_wallets.id"))
    amount = Column(Float)
    category = Column(String)
    wallet = relationship("Wallet", back_populates="expenses")