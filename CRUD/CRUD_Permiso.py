from schemas.Permiso import (
    PermisoCreate,
    Permiso,
    PermisoUpdate
)
from models import Permiso
from sqlalchemy.orm import Session

def crear_permiso(permiso_in: PermisoCreate, db: Session):
        db_permiso = Permiso(**permiso_in.dict())
        db.add(db_permiso)
        db.commit()
        db.refresh(db_permiso)
        return db_permiso


def listar_permiso(db: Session):
    return db.query(Permiso).all()


def actualizar_permiso(id_permiso: int, permiso_in: PermisoUpdate, db: Session):
    db_permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()
    if not db_permiso:
        raise Exception("Permiso no encontrado")
    # Actualizar solo los campos enviados en la petición
    for field, value in permiso_in.dict(exclude_unset=True).items():
        setattr(permiso_in, field, value)
    
    db.commit()
    db.refresh(permiso_in)
    return permiso_in

def eliminar_permiso(id_permiso: int, db: Session):
    db_permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()
    if not db_permiso:
        raise Exception("Permiso no encontrado")
    
    db.delete(db_permiso)
    db.commit()
    return db_permiso

def permiso_existente(db: Session, permiso_nombre: str):
    return db.query(Permiso).filter(Permiso.nombre == permiso_nombre).first()
