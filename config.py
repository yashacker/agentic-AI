from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

VECTOR_DB_PATH = str(
    BASE_DIR / "vector_db"
)