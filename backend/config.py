import os

class Config:
    SECRET_KEY = "super-secret-key"

    # Ejemplo con SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
