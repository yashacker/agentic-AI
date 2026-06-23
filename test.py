# test_retriever.py

from rag.retriever import retrieve

context = retrieve(
    "python calculator"
)

print(context)