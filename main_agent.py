from agents.planner import create_plan
from agents.coder import generate_code
from agents.reviewer import review_code

from rag.retriever import retrieve

request = """
Create a Python calculator
"""

print("=" * 50)
print("USER REQUEST")
print("=" * 50)

print(request)

context = retrieve(request)

print("\n" + "=" * 50)
print("RAG CONTEXT")
print("=" * 50)

print(context[:1000])

plan = create_plan(request)

print(type(plan))
print(plan)
print("=" * 50)

print(plan)

for task in plan["tasks"]:

    print("\n" + "=" * 50)
    print("TASK")
    print("=" * 50)

    print(task)

    code = generate_code(
        task=task,
        context=context
    )

    print("\nCODE")
    print(code)

    review = review_code(code)

    print("\nREVIEW")
    print(review)