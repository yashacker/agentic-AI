import json

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def create_plan(user_request):

    prompt = f"""
You are a senior software architect.

Break this request into tasks.

Return ONLY JSON.

Example:

{{
  "tasks": [
    "Create calculator class",
    "Implement add",
    "Implement subtract"
  ]
}}

Request:

{user_request}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown fences
    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    print("RAW RESPONSE:")
    print(content)

    return json.loads(content)