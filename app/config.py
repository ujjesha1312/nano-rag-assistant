import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4.1-nano"

SYSTEM_PROMPT = """
You are NanoRAG Assistant.
Answer strictly using the provided context.
If the answer is not in the context, say so.
"""

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
