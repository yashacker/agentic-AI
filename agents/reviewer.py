from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

def review_code(code):

    prompt = f"""
Review this code.

Check:
- Bugs
- Security
- Readability
- Performance

CODE:

{code}
"""

    response = llm.invoke(prompt)

    return response.content