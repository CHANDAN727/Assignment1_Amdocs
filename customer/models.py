from database import Base
from sqlalchemy import Column,String, DateTime,Integer
from database import Base
import datetime
from sqlalchemy.sql import func


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String)
    customer_type=Column(String)
    created_on= Column(DateTime, default=datetime.datetime.now())

