from sqlalchemy import Column, VARCHAR, BOOLEAN, ForeignKey, INTEGER, TIMESTAMP, Integer
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

# 使用者欄位
class User_info(BASE):
    __tablename__ = 'user_info'
    name = Column(VARCHAR, nullable = False)
    user_id = Column(VARCHAR, nullable = False, primary_key = True, unique = True)
    points = Column(Integer, nullable = False)
    email = Column(VARCHAR, nullable = True)


class Emoji_info(BASE):
    __tablename__ = 'emoji_info'
    emoji_eng = Column(VARCHAR, nullable = False, primary_key = True, unique = True)
    emoji_id = Column(VARCHAR, nullable = False)
    emoji_name = Column(VARCHAR, nullable = True)


class Event_points(BASE):
    __tablename__ = 'event_points'
    name = Column(VARCHAR, ForeignKey("user_info.name"), nullable = False)
    user_id = Column(VARCHAR, ForeignKey("user_info.user_id"), nullable = False, primary_key = True, unique = True)
    team_buying = Column(Integer, nullable = False, default = 0)
    working_report = Column(Integer, nullable = False, default = 0)
    docs_apply = Column(Integer, nullable = False, default = 300)