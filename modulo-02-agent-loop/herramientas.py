# herramientas.py — las herramientas del asistente de la academia
from strands import tool
import db


@tool
def consultar_curso(curso_id: str) -> str:
    """Consulta la información de un curso por su ID.

    Args:
        curso_id: El identificador del curso, p. ej. "PY-101"
    """
    curso = db.obtener_uno(
        "SELECT nombre, precio_usd, duracion_horas FROM cursos WHERE curso_id = ?",
        (curso_id,),
    )
    if curso is None:
        validos = [c["curso_id"] for c in db.obtener_todos("SELECT curso_id FROM cursos")]
        return f"No existe el curso {curso_id}. IDs válidos: {validos}"
    return f"{curso['nombre']} — ${curso['precio_usd']} USD — {curso['duracion_horas']} horas"