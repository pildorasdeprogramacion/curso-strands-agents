# Módulo 3 — El arte de las herramientas: el backend completo

🎥 **Video de este módulo:** [https://youtu.be/huRreJ_pSYo]

En este módulo dominamos el **contrato de una herramienta** —lo único que el
modelo ve de tu código— y completamos el backend del asistente con cinco
herramientas sobre SQLite: cursos, estudiantes, inscripciones y reembolsos.

## Archivos

| Archivo | Responsabilidad |
|---|---|
| `crear_db.py` | Crea `academia.db` con cursos, estudiantes e inscripciones (se corre una vez) |
| `db.py` | Capa de acceso a datos — el único archivo que habla con la base de datos |
| `herramientas.py` | Las cinco herramientas del agente (`@tool`) |
| `main.py` | Ensamblaje del agente (`crear_agente`) y punto de entrada |

## Las cinco herramientas

| Herramienta | Responsabilidad |
|---|---|
| `listar_cursos` | Lista el catálogo completo de cursos de la academia |
| `consultar_curso` | Devuelve el detalle de un curso a partir de su ID |
| `buscar_estudiante` | Identifica a un estudiante a partir de su correo electrónico |
| `consultar_inscripciones` | Lista las inscripciones de un estudiante a partir de su ID |
| `procesar_reembolso` | Procesa un reembolso si cumple la política de 30 días |

## Cómo correrlo

```bash
# 1. Reconstruir el entorno (usa las versiones exactas del uv.lock)
uv sync

# 2. Tus credenciales de Bedrock (ver Módulo 1)
export AWS_BEARER_TOKEN_BEDROCK="tu_api_key"

# 3. Crear la base de datos (una única vez)
#    Las fechas de inscripción se generan dinámicamente respecto a hoy,
#    para que el ejemplo de reembolso siga funcionando dentro de un año.
uv run crear_db.py

# 4. IMPORTANTE: abre main.py y reemplaza "TU_MODEL_ID" por el model_id
#    que te dio tu script de diagnóstico del Módulo 1.
#    (Cada cuenta/región tiene sus modelos: verifica, no copies.)

# 5. Correr el asistente
uv run main.py
```

## Experimentos del video

- **Reembolso fuera de plazo:** cambia el prompt al correo del otro estudiante,
  cuya inscripción ya superó los 30 días, y observa cómo el agente explica el
  rechazo en lugar de fallar. Ese es el "404" de nuestra analogía.
- **Provocar un 500:** pásale a `procesar_reembolso` un ID que no sea un entero
  y observa la excepción capturada por Strands llegando de vuelta al modelo.
- **Poner un techo al agente:** añade el parámetro de límites a la invocación
  (máximo de vueltas del agent loop y de tokens) y baja el máximo de vueltas a 1
  para forzar un `stop_reason` distinto de `end_turn`.
- **Una tool de la comunidad:** importa `current_time` desde `strands_tools`,
  pásasela al agente y pregúntale la fecha de hoy.