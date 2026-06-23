from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_DB_PATH = str(
    BASE_DIR / "vector_db"
)

print("Using DB:", VECTOR_DB_PATH)

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

# Local embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to existing vector database
from config import VECTOR_DB_PATH

db = Chroma(
    collection_name="codebase",
    embedding_function=embeddings,
    persist_directory=VECTOR_DB_PATH
)
print("Collection count:", db._collection.count())
print("Using DB:", VECTOR_DB_PATH)
print("Documents in DB:", db._collection.count())
print(f"Documents in DB: {db._collection.count()}")

def retrieve(query: str, k: int = 5) -> str:

    try:
        results = db.similarity_search(
            query=query,
            k=k
        )

        print(f"Retrieved {len(results)} documents")

        if not results:
            return ""

        context_parts = []

        for i, doc in enumerate(results, start=1):

            file_path = doc.metadata.get(
                "path",
                "Unknown File"
            )

            content = doc.page_content[:3000]

            context_parts.append(
                f"""
========== DOCUMENT {i} ==========
FILE: {file_path}

CONTENT:
{content}
"""
            )

        return "\n".join(context_parts)

    except Exception as e:

        print(f"Retriever Error: {e}")

        return ""