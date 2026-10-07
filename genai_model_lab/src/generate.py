import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(query, context):

    prompt = f"""
Answer the user's question using only the provided context and try to explain better.

Answer the user's question using only the provided context.

Do not use outside knowledge.
If the context does not contain enough information to answer
the question, say: "I don't have enough information."

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content