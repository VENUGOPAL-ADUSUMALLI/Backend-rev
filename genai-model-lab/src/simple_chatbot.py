from src.chat_client import ChatClient


def main() -> None:
    llm = ChatClient()

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful backend development tutor. "
                "Explain concepts clearly and use examples."
            ),
        }
    ]

    print("Chatbot started. Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        result = llm.chat(messages)

        assistant_response = result["content"]

        print(f"\nAssistant: {assistant_response}")

        messages.append(
            {
                "role": "assistant",
                "content": assistant_response,
            }
        )


if __name__ == "__main__":
    main()