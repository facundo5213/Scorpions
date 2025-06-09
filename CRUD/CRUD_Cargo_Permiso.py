from sqlalchemy.orm import Session, joinedload
from models.Cargo import Cargo
from models.Permiso import Permiso

def asignar_permiso_a_cargo(db: Session, id_cargo: int, id_permiso: int):
    cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()

    if not cargo or not permiso:
        raise Exception("Cargo o Permiso no encontrado")

    if permiso in cargo.permisos:
        raise Exception("Este permiso ya está asignado al cargo")

    cargo.permisos.append(permiso)
    db.commit()
    db.refresh(cargo)

    return {"id_cargo": id_cargo, "id_permiso": id_permiso}

def obtener_permisos_por_cargo(db: Session, id_cargo: int):
    cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    if not cargo:
        return None
    return cargo.permisos

def eliminar_permiso_de_cargo(db: Session, id_cargo: int, id_permiso: int):
    cargo = db.query(Cargo).filter(Cargo.id_cargo == id_cargo).first()
    permiso = db.query(Permiso).filter(Permiso.id_permiso == id_permiso).first()

    if permiso in cargo.permisos:
        cargo.permisos.remove(permiso)
        db.commit()
    return cargo

def obtener_cargos_con_permisos(db: Session):
    return db.query(Cargo).options(joinedload(Cargo.permisos)).all()