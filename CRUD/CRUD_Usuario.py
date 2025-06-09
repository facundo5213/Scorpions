from schemas.Usuario import (UsuarioResponse, UsuarioUpdate, UsuarioCreate)
from models import Usuario
from sqlalchemy.orm import Session

def crear_Usuario(usuario_data: dict, db: Session):
    # Nota: Ahora la función espera un dict en lugar de un modelo Pydantic,
    # para evitar llamar a .dict() sobre un dict.
    db_usuario = Usuario(**usuario_data)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def listar_Usuario(db: Session):
    return db.query(Usuario).all()


def actualizar_Usuario(id_usuario: int, usuario_in: UsuarioUpdate, db: Session):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not db_usuario:
        raise Exception("Usuario no encontrado")
    
    # Verifica si usuario_in tiene método dict(), en caso de que sea un modelo Pydantic
    data = usuario_in.dict(exclude_unset=True) if hasattr(usuario_in, "dict") else usuario_in
    
    # Actualizar solo los campos enviados en la petición
    for field, value in data.items():
        setattr(db_usuario, field, value)
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def eliminar_Usuario(id_usuario: int, db: Session):
    db_usuario = db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    if not db_usuario:
        raise Exception("Usuario no encontrado")
    
    db.delete(db_usuario)
    db.commit()
    return db_usuario


def usuario_existente(db: Session, nombre_usuario: str):
    return db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()
