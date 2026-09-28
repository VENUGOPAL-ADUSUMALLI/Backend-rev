def recursive_split(text, chunk_size=300):
    if len(text) <= chunk_size:
        return [text.strip()]

    separators = ["\n\n", "\n", ". ", " "]

    for separator in separators:
        parts = text.split(separator)

        if len(parts) == 1:
            continue

        chunks = []
        current = ""

        for part in parts:
            part = part.strip()

            if not part:
                continue

            candidate = (
                current + separator + part
                if current
                else part
            )

            if len(candidate) <= chunk_size:
                current = candidate
            else:
                if current:
                    chunks.append(current.strip())

                current = part

        if current:
            chunks.append(current.strip())

        final_chunks = []

        for chunk in chunks:
            if len(chunk) <= chunk_size:
                final_chunks.append(chunk)
            else:
                final_chunks.extend(
                    recursive_split(chunk, chunk_size)
                )

        return final_chunks

    # Last resort: split on words
    words = text.split()

    chunks = []
    current = ""

    for word in words:
        candidate = current + " " + word if current else word

        if len(candidate) <= chunk_size:
            current = candidate
        else:
            if current:
                chunks.append(current)

            current = word

    if current:
        chunks.append(current)

    return chunks
def main():
    text = """
Django is a Python web framework.

It provides an ORM for database operations.

Django also provides authentication and authorization.

REST APIs can be built using Django REST Framework.

FastAPI is another Python framework commonly used for building APIs.
"""

    chunks = recursive_split(text, chunk_size=10)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i} ---")
        print(chunk)
        print(f"Length: {len(chunk)}")


if __name__ == "__main__":
    main()