# Módulo 2 — El Agent Loop: nace el asistente

🎥 **Video de este módulo:** [https://youtu.be/Z238QRhtnoY]

En este módulo entendemos el motor de todo agente —el **Agent Loop**— y nace
nuestro asistente de la academia con su primera herramienta conectada a una
base de datos SQLite.

## Archivos

| Archivo | Responsabilidad |
|---|---|
| `crear_db.py` | Crea `academia.db` con los datos de ejemplo (se corre una vez) |
| `db.py` | Capa de acceso a datos — el único archivo que habla con la base de datos |
| `herramientas.py` | Las herramientas del agente (`@tool`) |
| `main.py` | Ensamblaje del agente (`crear_agente`) y punto de entrada |

## Cómo correrlo

```bash
# 1. Reconstruir el entorno (usa las versiones exactas del uv.lock)
uv sync

# 2. Tus credenciales de Bedrock (ver Módulo 1)
export AWS_BEARER_TOKEN_BEDROCK="tu_api_key"

# 3. Crear la base de datos (una única vez)
uv run crear_db.py

# 4. IMPORTANTE: abre main.py y reemplaza "TU_MODEL_ID" por el model_id
#    que te dio tu script de diagnóstico del Módulo 1.
#    (Cada cuenta/región tiene sus modelos: verifica, no copies.)

# 5. Correr el asistente
uv run main.py
```

## Experimentos del video

- **Leerle la mente al agente:** descomenta el bloque del `print` de
  `agente.messages` en `main.py` y observa el historial completo.
- **Provocar un error:** cambia la pregunta a `"¿Cuánto cuesta el curso ZZ-999?"`
  y observa cómo el agente se recupera solo.