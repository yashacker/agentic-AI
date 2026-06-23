from pathlib import Path

def list_files(root="."):

    files = []

    for file in Path(root).rglob("*"):

        if file.is_file():

            files.append(
                str(file)
            )

    return files