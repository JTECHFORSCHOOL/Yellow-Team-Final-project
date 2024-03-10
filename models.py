from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

    # Define relationships with other models
    bookings = relationship("Booking", back_populates="user")
    feedbacks = relationship("Feedback", back_populates="user")
    payments = relationship("Payment", back_populates="user")

class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    pickup_location = Column(String)
    dropoff_location = Column(String)

    # Define relationship with User
    user = relationship("User", back_populates="bookings")

class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    vehicle = Column(String)

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    rating = Column(Integer)
    comment = Column(String)

    # Define relationship with User
    user = relationship("User", back_populates="feedbacks")

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    status = Column(String)

    # Define relationship with User
    user = relationship("User", back_populates="payments")
