from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
from langchain_core.documents import Document

from indexer import load_files

load_dotenv()

docs = load_files("../")
from config import VECTOR_DB_PATH

db = Chroma(
    collection_name="codebase",
    embedding_function=embeddings,
    persist_directory=VECTOR_DB_PATH
)
print("Using DB:", VECTOR_DB_PATH)

documents = []

for doc in docs:

    documents.append(
        Document(
            page_content=doc["content"],
            metadata={
                "path": doc["path"]
            }
        )
    )

db.add_documents(documents)
print("Collection count:", db._collection.count())

print(f"Indexed {len(documents)} files")