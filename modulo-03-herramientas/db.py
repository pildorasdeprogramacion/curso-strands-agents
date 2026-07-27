# db.py — capa de acceso a datos de la academia
import os
import sqlite3
from contextlib import closing

DB_PATH = os.getenv("ACADEMIA_DB", "academia.db")


def _conectar() -> sqlite3.Connection:
    """Abre una conexión con acceso a las columnas por nombre."""
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def obtener_uno(sql: str, parametros: tuple = ()) -> dict | None:
    """Ejecuta un SELECT y retorna la primera fila como diccionario, o None si no hay resultados."""
    with closing(_conectar()) as conexion:
        fila = conexion.execute(sql, parametros).fetchone()
        return dict(fila) if fila else None


def obtener_todos(sql: str, parametros: tuple = ()) -> list[dict]:
    """Ejecuta un SELECT y retorna todas las filas como lista de diccionarios."""
    with closing(_conectar()) as conexion:
        filas = conexion.execute(sql, parametros).fetchall()
        return [dict(f) for f in filas]


def ejecutar(sql: str, parametros: tuple = ()) -> int:
    """Ejecuta un INSERT, UPDATE o DELETE y retorna el número de filas afectadas."""
    with closing(_conectar()) as conexion:
        cursor = conexion.execute(sql, parametros)
        conexion.commit()
        return cursor.rowcount