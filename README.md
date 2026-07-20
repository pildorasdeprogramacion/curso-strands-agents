# Curso de Strands Agents (AWS) — en Español 🇨🇴

Código oficial del curso de **Píldoras de Programación** sobre [Strands Agents](https://strandsagents.com),
el SDK open source de AWS para construir agentes de IA en Python.

A lo largo del curso construimos, módulo a módulo, un solo proyecto:
**el asistente virtual de una academia de cursos online** — con herramientas,
base de datos, aprobación humana, memoria, multi-agente y despliegue.

🎥 **Playlist del curso:** [ENLACE A TU PLAYLIST]

## Requisitos

- Python 3.10+ (lo gestiona `uv` automáticamente)
- [uv](https://docs.astral.sh/uv/) instalado
- Credenciales de Amazon Bedrock (ver Módulo 1) — o un proveedor alternativo:
  el curso también funciona con Ollama (local, gratis) o Gemini (API key gratuita)

## Cómo usar este repositorio

Cada módulo es una **carpeta autocontenida** con el proyecto en su estado final.
No necesitas los módulos anteriores para correr uno:

```bash
git clone https://github.com/TU_USUARIO/curso-strands-agents.git
cd curso-strands-agents/modulo-02-agent-loop
uv sync                                    # reconstruye el entorno exacto
export AWS_BEARER_TOKEN_BEDROCK="tu_key"   # tus credenciales (Módulo 1)
uv run crear_db.py                         # crea la base de datos (una vez)
uv run main.py                             # corre el asistente
```

Cada carpeta tiene su propio README con las instrucciones específicas del módulo.

## Índice de módulos

| Módulo | Carpeta | Video |
|---|---|---|
| 0 — Introducción: agentes y model-driven | (sin código) | [ver video](#) |
| 1 — Setup: uv, credenciales y primer agente | [`modulo-01-setup`](./modulo-01-setup) | [ver video](#) |
| 2 — El Agent Loop: nace el asistente | [`modulo-02-agent-loop`](./modulo-02-agent-loop) | [ver video](#) |

*(El índice crece a medida que se publican los módulos.)*

## ⚠️ Sobre las credenciales

Ningún archivo de este repo contiene llaves ni tokens. Tus credenciales van en
variables de entorno de TU máquina y **nunca** deben subirse a un repositorio.

## Licencia

MIT — usa, adapta y comparte este código libremente.