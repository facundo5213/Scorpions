# models/Usuario.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from db.base import Base
import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class Usuario(Base):
    __tablename__ = "usuario"
# models/Usuario.py
    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    contraseña = Column(String(150), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    telefono = Column(Integer, nullable=True)
    id_cargo = Column(Integer, ForeignKey("cargo.id_cargo"), nullable=True)
    estado = Column(Boolean, nullable=False, default=True)
    fecha_registro = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    # Relación con Cargo (esto debe coincidir con el back_populates en Cargo)
    cargo = relationship("Cargo", back_populates="usuarios")
