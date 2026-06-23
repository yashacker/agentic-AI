
from pathlib import Path

def read_file(path: str):

    try:
        return Path(path).read_text(
            encoding="utf-8"
        )

    except Exception as e:
        return f"Error: {e}"