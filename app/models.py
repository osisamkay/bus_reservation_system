
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import uuid
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    # Define relationship with Reservation model
    reservations = relationship("Reservation", back_populates="user")


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String(36), primary_key=True, default=str(
        uuid.uuid4()), unique=True, index=True)
    passenger_name = Column(String)
    seat_number = Column(Integer)
    user_id = Column(String(36), ForeignKey("users.id"))
    bus_id = Column(String(36), ForeignKey("buses.id"))

    # Relationships with User and Bus tables
    user = relationship("User", back_populates="reservations")
    bus = relationship("Bus", back_populates="reservations")


class Bus(Base):
    __tablename__ = "buses"

    id = Column(String(36), primary_key=True, default=str(
        uuid.uuid4()), unique=True, index=True)
    bus_number = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    route = Column(String)

    # Relationship with Reservation table
    reservations = relationship("Reservation", back_populates="bus")


class Price(Base):
    __tablename__ = "prices"

    id = Column(String(36), primary_key=True, default=str(
        uuid.uuid4()), unique=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.id"))
    bus_type = Column(String)
    price = Column(Float)

    # Relationship with Route table
    route = relationship("Route", back_populates="prices")


class Route(Base):
    __tablename__ = "routes"

    id = Column(String(36), primary_key=True, default=lambda: str(
        uuid.uuid4()), unique=True, index=True)
    source = Column(String)
    destination = Column(String)

    # Relationship with Price table
    prices = relationship("Price", back_populates="route")
1