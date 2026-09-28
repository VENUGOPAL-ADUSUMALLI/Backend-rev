import os
from typing import Any

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


class GroqClient:
    def __init__(self,
        model: str = "openai/gpt-oss-20b",
        temperature: float = 0.2,
        max_tokens: int = 500,
    ) -> None:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY is missing from .env")

        self.client = Groq(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(
        self,
        system_message: str,
        user_message: str,
    ) -> dict[str, Any]:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_message,
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        message = response.choices[0].message

        return {
            "content": message.content,
            "usage": response.usage,
            "model": self.model,
        }


if __name__ == "__main__":
    llm = GroqClient()

    result = llm.generate(
        system_message="You are a helpful GenAI tutor.",
        user_message="Explain embeddings in simple language.",
    )

    print("Assistant:")
    print(result)

    print("\nUsage:")
    print(result["usage"])