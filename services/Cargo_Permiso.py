from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Cargo import Cargo
from CRUD.CRUD_Cargo_Permiso import asignar_permiso_a_cargo, obtener_permisos_por_cargo, eliminar_permiso_de_cargo, obtener_cargos_con_permisos
from schemas.Cargo_Permiso import CargoConPermisos, PermisoSimple


def asignar_permiso_service(db: Session, id_cargo: int, id_permiso: int):
    try:
        return asignar_permiso_a_cargo(db, id_cargo, id_permiso)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def listar_permisos_por_cargo_service(db: Session, id_cargo: int):
    return obtener_permisos_por_cargo(db, id_cargo)

def eliminar_permiso_service(db: Session, id_cargo: int, id_permiso: int):
    try:
        return eliminar_permiso_de_cargo(db, id_cargo, id_permiso)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def listar_cargos_con_permisos_service(db: Session) -> list[CargoConPermisos]:
    cargos = obtener_cargos_con_permisos(db)
    return [
        CargoConPermisos(
            id_cargo=cargo.id_cargo,
            cargo=cargo.cargo,
            descripcion=cargo.descripcion,
            permisos=[
                PermisoSimple(
                    id_permiso=permiso.id_permiso,
                    nombre=permiso.nombre,
                    descripcion=permiso.descripcion
                )
                for permiso in cargo.permisos
            ]
        )
        for cargo in cargos
    ]
