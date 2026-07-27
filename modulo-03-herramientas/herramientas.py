# herramientas.py — las herramientas del asistente de la academia
from datetime import date, timedelta

from strands import tool

import db

DIAS_VENTANA_REEMBOLSO = 30


@tool
def listar_cursos() -> str:
    """Lista el catálogo completo de cursos disponibles en la academia.

    Returns:
        Un listado con el ID, nombre, precio y duración de cada curso.
    """
    cursos = db.obtener_todos("SELECT * FROM cursos ORDER BY curso_id")
    lineas = [
        f"{c['curso_id']}: {c['nombre']} — ${c['precio_usd']} USD — {c['duracion_horas']} horas"
        for c in cursos
    ]
    return "\n".join(lineas)


@tool
def consultar_curso(curso_id: str) -> str:
    """Consulta la información detallada de un curso específico por su ID.

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


@tool
def buscar_estudiante(email: str) -> str:
    """Identifica a un estudiante de la academia a partir de su correo electrónico.

    Args:
        email: El correo con el que el estudiante se registró, p. ej. "maria@example.com"

    Returns:
        El ID y nombre del estudiante, necesarios para consultar sus inscripciones.
    """
    estudiante = db.obtener_uno(
        "SELECT estudiante_id, nombre FROM estudiantes WHERE email = ?",
        (email.strip().lower(),),
    )
    if estudiante is None:
        return f"No hay ningún estudiante registrado con el correo {email}."
    return f"Estudiante {estudiante['estudiante_id']}: {estudiante['nombre']}"


@tool
def consultar_inscripciones(estudiante_id: str) -> str:
    """Consulta los cursos en los que está inscrito un estudiante, con fechas y estado.

    Args:
        estudiante_id: El ID del estudiante, p. ej. "E-001" (se obtiene con buscar_estudiante)
    """
    inscripciones = db.obtener_todos(
        """SELECT i.inscripcion_id, c.nombre, i.fecha_inscripcion, i.estado
           FROM inscripciones i JOIN cursos c ON c.curso_id = i.curso_id
           WHERE i.estudiante_id = ?""",
        (estudiante_id,),
    )
    if not inscripciones:
        return f"El estudiante {estudiante_id} no tiene inscripciones."
    lineas = [
        f"Inscripción {i['inscripcion_id']}: {i['nombre']} — inscrito el {i['fecha_inscripcion']} — estado: {i['estado']}"
        for i in inscripciones
    ]
    return "\n".join(lineas)


@tool
def procesar_reembolso(inscripcion_id: int) -> str:
    """Procesa el reembolso de una inscripción, si cumple la política de la academia.

    La política permite reembolsos hasta 30 días después de la fecha de inscripción.

    Args:
        inscripcion_id: El número de la inscripción a reembolsar (se obtiene con consultar_inscripciones)

    Returns:
        Confirmación con el monto reembolsado, o el motivo por el cual no procede.
    """
    # Violación de contrato → raise (el "500"): Strands lo convierte en un resultado de error
    if inscripcion_id <= 0:
        raise ValueError("El inscripcion_id debe ser un entero positivo.")

    inscripcion = db.obtener_uno(
        """SELECT i.inscripcion_id, i.fecha_inscripcion, i.estado, c.nombre, c.precio_usd
           FROM inscripciones i JOIN cursos c ON c.curso_id = i.curso_id
           WHERE i.inscripcion_id = ?""",
        (inscripcion_id,),
    )

    # Resultados de dominio → return informativo (los "404")
    if inscripcion is None:
        return f"No existe la inscripción {inscripcion_id}."
    if inscripcion["estado"] == "reembolsada":
        return f"La inscripción {inscripcion_id} ya fue reembolsada anteriormente."

    # Regla de negocio DETERMINISTA: la fecha se compara en código, no la compara el modelo
    fecha_inscripcion = date.fromisoformat(inscripcion["fecha_inscripcion"])
    fecha_limite = fecha_inscripcion + timedelta(days=DIAS_VENTANA_REEMBOLSO)
    if date.today() > fecha_limite:
        return (
            f"El reembolso no es elegible: la inscripción es del {fecha_inscripcion} "
            f"y la ventana de {DIAS_VENTANA_REEMBOLSO} días venció el {fecha_limite}."
        )

    db.ejecutar(
        "UPDATE inscripciones SET estado = 'reembolsada' WHERE inscripcion_id = ?",
        (inscripcion_id,),
    )
    return (
        f"Reembolso procesado: {inscripcion['nombre']} — "
        f"${inscripcion['precio_usd']} USD devueltos al estudiante."
    )