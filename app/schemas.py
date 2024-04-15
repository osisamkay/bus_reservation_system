from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4


class ReservationBase(BaseModel):
    passenger_name: str
    seat_number: int
    user_id: UUID4
    bus_id: UUID4


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: UUID4


class BusBase(BaseModel):
    bus_number: str
    capacity: int
    route: str


class BusCreate(BusBase):
    pass


class Bus(BusBase):
    id: UUID4


class PriceBase(BaseModel):
    bus_type: str
    price: float
    route_id: UUID4


class PriceCreate(PriceBase):
    pass


class Price(PriceBase):
    id: UUID4


class RouteBase(BaseModel):
    source: str
    destination: str


class RouteCreate(BaseModel):
    source: str
    destination: str


class RouteUpdate(BaseModel):
    source: str
    destination: str


class Route(RouteBase):
    id: UUID4
