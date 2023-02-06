from sqlalchemy import Column, VARCHAR, BOOLEAN, ForeignKey, INTEGER, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

# 使用者欄位
class User_info(BASE):
    __tablename__ = 'user_info'
    name = Column(VARCHAR, nullable = False)
    user_id = Column(VARCHAR, nullable = False, primary_key = True, unique = True)
    points = Column(Integer, nullable = False)
