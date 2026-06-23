

from pathlib import Path

def write_file(
    path: str,
    content: str
):

    try:

        Path(path).write_text(
            content,
            encoding="utf-8"
        )

        return f"Saved {path}"

    except Exception as e:

        return f"Error: {e}"