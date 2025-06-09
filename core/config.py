# core/config.py
from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Carga explícita del archivo "archivo.env"
load_dotenv("Seguridad.env")

class Settings(BaseSettings):
    PROJECT_NAME: str = "Proyecto_Prueba"
    DATABASE_URL: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return self.DATABASE_URL

    class Config:
        # Indicamos que use "archivo.env" en lugar de ".env"
        env_file = "Seguridad.env"

settings = Settings()
