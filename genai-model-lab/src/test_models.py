from src.groq_client import GroqClient

MODELS = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
    "qwen/qwen3.8-27b",
]
prompt = """ 
Explain what Retrieval-Augmented Generation is
in exactly 3 simple bullet points.
"""
for model_name in MODELS:
    print("=" * 70)
    print(f"MODEL: {model_name}")
    print("=" * 70)
    try:
        llm = GroqClient(
            model=model_name,
            temperature=0.2,
            max_tokens=300,
        )
        result = llm.generate(
            system_message="you are are a helpful GenAI tutor",
            user_message= prompt,
        )
        print(result["content"])
        print("\nUSAGE:")
        print(result["usage"])
    except Exception as error:
        print(f"ERROR: {type(error).__name__}: {error}")

