# models/Permiso.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base
from db.associations import cargo_permiso

class Permiso(Base):
    __tablename__ = "permiso"
    id_permiso  = Column(Integer, primary_key=True, autoincrement=True)
    nombre      = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(150), nullable=True)

    cargos = relationship(
        "Cargo",
        secondary=cargo_permiso,
        back_populates="permisos"
    )
