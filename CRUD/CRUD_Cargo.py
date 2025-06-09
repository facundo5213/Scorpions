from schemas.Cargo import (
    CargoCreate,
    Cargo,
    CargoUpdate
)
from models import Cargo
from sqlalchemy.orm import Session

def crear_cargo(cargo_in: CargoCreate, db: Session):
        db_cargo = Cargo(**cargo_in.dict())
        db.add(db_cargo)
        db.commit()
        db.refresh(db_cargo)
        return db_cargo


def listar_cargo(db: Session):
    return db.query(Cargo).all()


def actualizar_cargo(id_cargo: int, cargo_in: CargoUpdate, db: Session):
    db_cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not db_cargo:
        raise Exception("Cargo no encontrado")
    # Actualizar solo los campos enviados en la petición
    for field, value in cargo_in.dict(exclude_unset=True).items():
        setattr(db_cargo, field, value)
    
    db.commit()
    db.refresh(db_cargo)
    return db_cargo

def eliminar_cargo(id_cargo: int, db: Session):
    db_cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not db_cargo:
        raise Exception("Cargo no encontrado")
    
    db.delete(db_cargo)
    db.commit()
    return db_cargo

def cargo_existente(db: Session, cargo_nombre: str):
    return db.query(Cargo).filter(Cargo.cargo == cargo_nombre).first()


def obtener_cargo_nombre(nombre_cargo: str, db: Session):
    return db.query(Cargo).filter(Cargo.cargo == nombre_cargo).first()

