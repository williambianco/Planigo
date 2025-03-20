from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    availability = Column(String, nullable=False)

class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True)
    day = Column(String, nullable=False)
    time = Column(String, nullable=False)
    role_needed = Column(String, nullable=False)
    assigned_employee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    assigned_employee = relationship("Employee")
