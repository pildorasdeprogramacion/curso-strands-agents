# main.py — ensamblaje y punto de entrada del asistente
from strands import Agent
from config import get_model

from herramientas import (
    buscar_estudiante,
    consultar_curso,
    consultar_inscripciones,
    listar_cursos,
    procesar_reembolso,
)

SYSTEM_PROMPT = """Eres el asistente virtual de una academia de cursos online.
Atiendes a estudiantes en español, de forma clara y amable.
Antes de consultar inscripciones o procesar reembolsos, identifica al estudiante por su correo."""


def crear_agente() -> Agent:
    """Crea y configura el asistente de la academia."""
    return Agent(
        model=get_model(),
        system_prompt=SYSTEM_PROMPT,
        tools=[listar_cursos, consultar_curso, buscar_estudiante,
               consultar_inscripciones, procesar_reembolso],
    )


if __name__ == "__main__":
    agente = crear_agente()
    agente("Soy maria@example.com. y quiero cancelar la incripcion del curso Agentes de IA con Strands")