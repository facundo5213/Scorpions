from pydantic import BaseModel
from typing import List

class CargoPermisoBase(BaseModel):
    id_cargo: int
    id_permiso: int

class CargoPermisoCreate(CargoPermisoBase):
    pass

class CargoPermisoResponse(CargoPermisoBase):
    class Config:
        from_attributes = True

class PermisoSimple(BaseModel):
    id_permiso: int
    nombre: str
    descripcion: str

    class Config:
        from_attributes = True

class CargoConPermisos(BaseModel):
    id_cargo: int
    cargo: str
    descripcion: str
    permisos: List[PermisoSimple]

    class Config:
        from_attributes = True
