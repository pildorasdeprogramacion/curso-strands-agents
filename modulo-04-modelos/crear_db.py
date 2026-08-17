# crear_db.py — crea la base de datos de la academia con datos de ejemplo
import sqlite3
from datetime import date, timedelta

conexion = sqlite3.connect("academia.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    curso_id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio_usd REAL NOT NULL,
    duracion_horas INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    estudiante_id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inscripciones (
    inscripcion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudiante_id TEXT NOT NULL REFERENCES estudiantes(estudiante_id),
    curso_id TEXT NOT NULL REFERENCES cursos(curso_id),
    fecha_inscripcion TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'activa'   -- 'activa' | 'reembolsada'
)
""")

cursor.executemany(
    "INSERT OR REPLACE INTO cursos VALUES (?, ?, ?, ?)",
    [
        ("PY-101", "Python desde cero", 49, 12),
        ("AG-201", "Agentes de IA con Strands", 79, 8),
        ("JS-110", "JavaScript moderno", 59, 15),
    ],
)

cursor.executemany(
    "INSERT OR REPLACE INTO estudiantes VALUES (?, ?, ?)",
    [
        ("E-001", "María Gómez", "maria@example.com"),
        ("E-002", "Carlos Ruiz", "carlos@example.com"),
    ],
)

# Fechas RELATIVAS a hoy, para que las demos funcionen siempre:
hace_10_dias = (date.today() - timedelta(days=10)).isoformat()   # elegible para reembolso
hace_45_dias = (date.today() - timedelta(days=45)).isoformat()   # fuera de la ventana de 30 días

cursor.execute("DELETE FROM inscripciones")
cursor.executemany(
    "INSERT INTO inscripciones (estudiante_id, curso_id, fecha_inscripcion, estado) VALUES (?, ?, ?, ?)",
    [
        ("E-001", "AG-201", hace_10_dias, "activa"),        # id 1: reembolso ELEGIBLE
        ("E-001", "PY-101", hace_45_dias, "activa"),        # id 2: reembolso NO elegible (ventana)
        ("E-002", "JS-110", hace_10_dias, "reembolsada"),   # id 3: ya reembolsada
    ],
)

conexion.commit()
conexion.close()
print("Base de datos academia.db creada con datos de ejemplo")