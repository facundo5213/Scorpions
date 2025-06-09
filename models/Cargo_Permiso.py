from sqlalchemy import Table, Column, Integer, ForeignKey
from db.base import Base

cargo_permiso = Table(
    "cargo_permiso",
    Base.metadata,
    Column("id_cargo", Integer, ForeignKey("cargo.id_cargo"), primary_key=True),
    Column("id_permiso", Integer, ForeignKey("permiso.id_permiso"), primary_key=True)
)
