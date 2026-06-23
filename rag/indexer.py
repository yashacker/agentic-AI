from pathlib import Path

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".html",
    ".css",
    ".json",
    ".md"
}

def load_files(root="."):

    docs = []

    for file in Path(root).rglob("*"):

        if file.suffix in SUPPORTED_EXTENSIONS:

            try:
                docs.append(
                    {
                        "path": str(file),
                        "content": file.read_text(
                            encoding="utf-8",
                            errors="ignore"
                        )
                    }
                )

            except Exception:
                pass

    return docs