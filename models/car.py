from dataclasses import dataclass


@dataclass
class Engine:
    volume: int
    fuel: str


@dataclass
class Transmission:
    type: str
    fwd: bool


@dataclass()
class Price:
    base_price: int
    tax: float
    discount: float


@dataclass()
class Car:
    manufacturer: str
    model: str
    type: str
    color: str
    trim: str
    year: int
    mileage: int
    engine: Engine
    price: Price
