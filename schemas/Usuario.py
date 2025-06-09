# app/schemas/persona.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


#Estos son los datos que recibes del cliente

#Contiene los campos comunes que el cliente envía
class UsuarioBase(BaseModel):
    nombre_usuario: str
    contraseña: str
    nombre: str
    apellido: str
    email: str
    telefono: int


#Heredan de UsuarioBase y definen lo que se espera en las peticiones de creación o actualización
class UsuarioCreate(UsuarioBase):
    cargo: Optional[str] = None
    
class UsuarioUpdate(UsuarioBase):
    nombre_usuario: Optional[str] = None
    contraseña: Optional[str] = None
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[int] = None
    cargo: Optional[str] = None


#Extiende de UsuarioBase e incluye los identificadores que la base de datos genera
class UsuarioInDBBase(UsuarioBase):
    id_usuario: int
    id_cargo: int

#Hereda de UsuarioInDBBase para usarla en las respuestas de la API
    class Config:
        orm_mode = True

# Schema de respuesta; lo puedes llamar también UsuarioResponse
class UsuarioResponse(UsuarioInDBBase):
    fecha_registro: datetime
