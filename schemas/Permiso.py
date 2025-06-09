# app/schemas/persona.py
from pydantic import BaseModel
from typing import Optional

class PermisoBase(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class PermisoCreate(PermisoBase):
    pass

class PermisoUpdate(PermisoBase):
    pass

class PermisoInDBBase(PermisoBase):
    id_permiso: int

    class Config:
        orm_mode = True

# Schema de respuesta
class Permiso(PermisoInDBBase):
    pass
