import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def create_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

text = "Django is a Python web framework."

embedding = create_embedding(text)

print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])