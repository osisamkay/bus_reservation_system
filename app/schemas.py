from typing import Optional
from pydantic import BaseModel, UUID4
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


class ReservationBase(BaseModel):
    passenger_name: str
    seat_number: int
    user_id: UUID4
    bus_id: UUID4

    class Config:
        orm_mode = True


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: UUID4

    class Config:
        orm_mode = True


class BusBase(BaseModel):
    bus_number: str
    capacity: int
    route: str

    class Config:
        orm_mode = True


class BusCreate(BusBase):
    pass


class Bus(BusBase):
    id: UUID4

    class Config:
        orm_mode = True


class PriceBase(BaseModel):
    bus_type: str
    price: float
    route_id: UUID4

    class Config:
        orm_mode = True


class PriceCreate(PriceBase):
    pass


class Price(PriceBase):
    id: UUID4

    class Config:
        orm_mode = True


class RouteBase(BaseModel):
    source: str
    destination: str

    class Config:
        orm_mode = True


class RouteCreate(RouteBase):
    pass


class Route(RouteBase):
    id: UUID4

    class Config:
        orm_mode = True
