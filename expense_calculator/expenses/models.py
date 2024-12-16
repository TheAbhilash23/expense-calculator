from sqlalchemy import Column, BigInteger, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from expense_calculator.core.db import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(BigInteger, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    description = Column(String(255))
    date = Column(DateTime)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="expenses")

