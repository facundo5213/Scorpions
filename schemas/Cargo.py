# app/schemas/persona.py
from pydantic import BaseModel
from typing import Optional

class CargoBase(BaseModel):
    cargo: Optional[str] = None
    descripcion: Optional[str] = None


class CargoCreate(CargoBase):
    pass

class CargoUpdate(CargoBase):
    pass

class CargoInDBBase(CargoBase):
    id_cargo: int

    class Config:
        orm_mode = True

# Schema de respuesta
class Cargo(CargoInDBBase):
    pass
