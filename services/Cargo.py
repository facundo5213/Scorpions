from sqlalchemy.orm import Session
from CRUD.CRUD_Cargo import cargo_existente, crear_cargo, listar_cargo, actualizar_cargo, eliminar_cargo    

# definen la estructura de los datos necesarios para crear y actualizar un cargo.
from schemas.Cargo import CargoCreate, CargoUpdate
from models import Cargo 
from fastapi import HTTPException

def Registrar_cargo(cargo_data: CargoCreate, db: Session) -> Cargo:
    # Aseguramos pasar el valor correcto (cargo_data.cargo, que debe ser un string)
    if cargo_existente(db, cargo_data.cargo):
        raise HTTPException(status_code=400, detail="El cargo ya existe")
    return crear_cargo(cargo_data, db)

def Listar_cargo(db):
    return listar_cargo(db)


def Actualizar_cargo(id_cargo: int, cargo_in: CargoUpdate, db: Session) -> Cargo:
    db_cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not db_cargo:
        raise HTTPException(status_code=404, detail="Cargo no encontrado.")
    for field, value in cargo_in.dict(exclude_unset=True).items():
        setattr(db_cargo, field, value)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo

def Eliminar_cargo(id_cargo: int, db):
    return eliminar_cargo(id_cargo, db)


