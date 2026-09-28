import os
from typing import Any

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class ChatClient:
    def __init__(
        self,
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

    def chat(self, messages: list[dict[str, str]]) -> dict[str, Any]:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        return {
            "content": response.choices[0].message.content,
            "usage": response.usage,
            "model": self.model,
        }


if __name__ == "__main__":
    llm = ChatClient()

    conversation = [
        {
            "role": "system",
            "content": "You are a helpful Python tutor.",
        },
        {
            "role": "user",
            "content": "What is a Python decorator?",
        },
        {
            "role": "assistant",
            "content": (
                "A decorator is a function that modifies "
                "the behavior of another function."
            ),
        },
        {
            "role": "user",
            "content": "Show me a simple example.",
        },
    ]

    result = llm.chat(conversation)

    print("Assistant:")
    print(result["content"])