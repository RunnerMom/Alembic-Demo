from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy import ForeignKey

engine = create_engine("sqlite:///runcoach.db", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()

""" 
The 3 classes below are tables in our runcoach.db
"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    token = Column(String(64), nullable=True)
    request_id = Column(String(64), nullable=True)
    ath_profile_id = Column(Integer, nullable=True)

class Assignment(Base):
    import datetime
    __tablename__= "assignments"     # tables hold daily running assigments

    id = Column(Integer, primary_key = True)
    date= Column(Date, nullable = True)   # calendar date stored as string
    workout_id = Column(Integer, ForeignKey('workouts.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    total_miles_assigned = Column(Float(1))
    total_time_assigned = Column(DateTime)
    

class Workout(Base):             
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    workout_type = Column(Integer, nullable=True)
    pace = Column(String(16), nullable=True)
    workout_time = Column(Integer, nullable=True) #store number of seconds
### End class declarations


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
