from sqlalchemy.orm import Session
from CRUD.CRUD_Usuario import crear_Usuario, listar_Usuario, actualizar_Usuario, eliminar_Usuario, usuario_existente    
from CRUD.CRUD_Cargo import obtener_cargo_nombre
# definen la estructura de los datos necesarios para crear y actualizar un cargo.
from schemas.Usuario import UsuarioCreate, UsuarioUpdate
from models import Usuario 
from fastapi import HTTPException


def Registrar_usuario(usuario_data: UsuarioCreate, db: Session) -> Usuario:
    # Verifica que no exista ya un usuario con ese nombre
    if usuario_existente(db, usuario_data.nombre_usuario):
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Busca el cargo por su nombre; se espera que usuario_data.cargo sea un string
    cargo_usuario = obtener_cargo_nombre(usuario_data.cargo, db)
    if not cargo_usuario:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    
    # Convertir el modelo Pydantic a dict
    datos_usuario = usuario_data.dict()
    # Reemplaza el campo 'cargo' (nombre) por 'id_cargo'
    datos_usuario['id_cargo'] = cargo_usuario.id_cargo
    # Elimina el campo 'cargo', si ya no es necesario
    datos_usuario.pop('cargo', None)
    
    return crear_Usuario(datos_usuario, db)

def Listar_usuario(db):
    return listar_Usuario(db)


def Actualizar_usuario(id_usuario: int, usuario_data: UsuarioUpdate, db: Session) -> Usuario:
    if usuario_existente(db, usuario_data.nombre_usuario):
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    cargo_usuario = obtener_cargo_nombre(usuario_data.cargo, db)
    if not cargo_usuario:
        raise HTTPException(status_code=404, detail="Cargo no encontrado")
    
    # Convertir el modelo Pydantic a dict
    datos_usuario = usuario_data.dict()
    # Reemplaza el campo 'cargo' (nombre) por 'id_cargo'
    datos_usuario['id_cargo'] = cargo_usuario.id_cargo
    # Elimina el campo 'cargo', si ya no es necesario
    datos_usuario.pop('cargo', None)


    return actualizar_Usuario(id_usuario, datos_usuario, db)

def Eliminar_usuario(id_usuario: int, db):
    return eliminar_Usuario(id_usuario, db)
