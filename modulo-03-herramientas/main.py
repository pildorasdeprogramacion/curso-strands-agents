# main.py — ensamblaje y punto de entrada del asistente
from strands import Agent
from strands.models import BedrockModel
from strands_tools import current_time

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
    modelo = BedrockModel(
        model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",   # el de su diagnóstico del Módulo 1
        region_name="us-east-2",
        temperature=0.3,
        max_tokens=1024,
    )
    return Agent(
        model=modelo,
        system_prompt=SYSTEM_PROMPT,
        tools=[listar_cursos, consultar_curso, buscar_estudiante,
               consultar_inscripciones, procesar_reembolso, current_time],
    )


if __name__ == "__main__":
    agente = crear_agente()
    agente("Soy maria@example.com. Quiero el reembolso de mi curso de agentes.")