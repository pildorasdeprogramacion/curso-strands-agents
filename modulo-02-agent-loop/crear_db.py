# crear_db.py — crea la base de datos de la academia con datos de ejemplo
import sqlite3

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

cursor.executemany(
    "INSERT OR REPLACE INTO cursos VALUES (?, ?, ?, ?)",
    [
        ("PY-101", "Python desde cero", 49, 12),
        ("AG-201", "Agentes de IA con Strands", 79, 8),
        ("JS-110", "JavaScript moderno", 59, 15),
    ],
)

conexion.commit()
conexion.close()
print("Base de datos academia.db creada con datos de ejemplo")