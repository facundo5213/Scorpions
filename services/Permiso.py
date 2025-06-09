from sqlalchemy.orm import Session
from CRUD.CRUD_Permiso import permiso_existente, crear_permiso, listar_permiso, actualizar_permiso, eliminar_permiso   

# definen la estructura de los datos necesarios para crear y actualizar un cargo.
from schemas.Permiso import PermisoCreate, PermisoUpdate
from models import Permiso
from fastapi import HTTPException

def Registrar_permiso(permiso_data: PermisoCreate, db: Session) -> Permiso:
    # Aseguramos pasar el valor correcto (cargo_data.cargo, que debe ser un string)
    if permiso_existente(db, permiso_data.nombre):
        raise HTTPException(status_code=400, detail="El Permiso ya existe")
    return crear_permiso(permiso_data, db)

def Listar_permiso(db):
    return listar_permiso(db)


def Actualizar_permiso(id_permiso: int, permiso_in: PermisoUpdate, db: Session) -> Permiso:
    db_permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()
    if not db_permiso:
        raise HTTPException(status_code=404, detail="Permiso no encontrado.")
    for field, value in permiso_in.dict(exclude_unset=True).items():
        setattr(db_permiso, field, value)
    db.commit()
    db.refresh(db_permiso)
    return db_permiso

def Eliminar_permiso(id_permiso: int, db):
    return eliminar_permiso(id_permiso, db)


