# models/Cargo.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base
from db.associations import cargo_permiso

class Cargo(Base):
    __tablename__ = "cargo"
    id_cargo    = Column(Integer, primary_key=True, autoincrement=True)
    cargo       = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(150), nullable=True)

    usuarios = relationship("Usuario", back_populates="cargo")
    permisos = relationship(
        "Permiso",
        secondary=cargo_permiso,
        back_populates="cargos"
    )
