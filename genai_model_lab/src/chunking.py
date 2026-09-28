def chunk_text(text, chunk_size=100, overlap=20):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap

    return chunks


def main():
    text = """
    Python is a programming language.
    It is widely used for backend development.
    Django is a popular Python web framework.
    Django provides an ORM for database operations.
    FastAPI is useful for building APIs.
    """

    chunks = chunk_text(text, chunk_size=100, overlap=20)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i} ---")
        print(chunk)


if __name__ == "__main__":
    main()