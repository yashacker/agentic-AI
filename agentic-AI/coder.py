from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def generate_code(task, context):

    prompt = f"""
You are an expert software engineer.

TASK:
{task}

REPOSITORY CONTEXT:
{context}

Generate code that follows
the existing project structure.

Return code only.
"""

    response = llm.invoke(prompt)

    return response.content