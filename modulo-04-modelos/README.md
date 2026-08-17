# Módulo 4 — El cerebro enchufable: Strands es agnóstico al modelo

**Video de este módulo:** https://youtu.be/U0HVnyQDRQ4

En este módulo demostramos que el asistente NO está casado con ningún proveedor:
nace `config.py` con `get_model()`, y el mismo asistente corre con Bedrock,
con un modelo local en tu máquina (Ollama), o con APIs gratuitas (Gemini, Groq...)
**cambiando una variable de entorno**. Las herramientas, la base de datos y los
contratos no cambian ni una línea.

## Archivos

| Archivo | Responsabilidad |
|---|---|
| `config.py` | **(Nuevo)** `get_model()`: elige el cerebro según `PROVEEDOR_MODELO` |
| `main.py` | Ensamblaje del agente — ahora con `model=get_model()` |
| `herramientas.py` | Las 5 herramientas del asistente (sin cambios desde el M3) |
| `db.py` | Capa de acceso a datos (sin cambios) |
| `crear_db.py` | Crea `academia.db` con datos de ejemplo (se corre una vez) |

## Cómo correrlo

```bash
uv sync
uv run crear_db.py        # una única vez
```

Luego elige tu cerebro:

**Opción A — Bedrock (default):**
```bash
export AWS_BEARER_TOKEN_BEDROCK="tu_api_key"
# Abre config.py y reemplaza "TU_MODEL_ID" por el de tu diagnóstico del Módulo 1
uv run main.py
```

**Opción B — Ollama (local, gratis):**
```bash
uv add 'strands-agents[ollama]'
ollama pull llama3.1      # o el modelo con soporte de tools que aguante tu máquina
export PROVEEDOR_MODELO=ollama
uv run main.py
```

**Opción C — Gemini (API gratuita, sin tarjeta):**
```bash
uv add 'strands-agents[gemini]'
export PROVEEDOR_MODELO=gemini
export GEMINI_API_KEY="tu_key_de_aistudio"
uv run main.py
```

## El experimento del video

Corre la misma pregunta con dos cerebros distintos (`PROVEEDOR_MODELO=bedrock`
vs `=ollama`) y compara cómo cada uno maneja la cadena de herramientas del
reembolso. Mismo código, distinta calidad — esa es la lección.