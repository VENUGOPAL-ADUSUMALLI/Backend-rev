from pathlib import Path

import chromadb

from load_document import load_document
from recursive_chunking import recursive_split
from openai_embeddings import create_embedding


def main():
    # -----------------------------
    # 1. Locate document
    # -----------------------------

    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "backend.txt"

    # -----------------------------
    # 2. Load document
    # -----------------------------

    text = load_document(file_path)

    # -----------------------------
    # 3. Split into chunks
    # -----------------------------

    chunks = recursive_split(
        text,
        chunk_size=300
    )

    print(f"Total chunks: {len(chunks)}")

    # -----------------------------
    # 4. Create embeddings
    # -----------------------------

    embeddings = []

    for i, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        embeddings.append(embedding)

        print(
            f"Chunk {i} → "
            f"embedding dimensions: {len(embedding)}"
        )

    # -----------------------------
    # 5. Create ChromaDB client
    # -----------------------------

    chroma_path = project_root / "chroma_db"

    client = chromadb.PersistentClient(
        path=str(chroma_path)
    )

    # -----------------------------
    # 6. Create collection
    # -----------------------------

    collection = client.get_or_create_collection(
        name="backend_documents"
    )

    # -----------------------------
    # 7. Create IDs
    # -----------------------------

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    # -----------------------------
    # 8. Store everything
    # -----------------------------

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {"source": "backend.txt"}
            for _ in chunks
        ]
    )

    print("\nStored successfully!")

    print(
        "Documents in collection:",
        collection.count()
    )


if __name__ == "__main__":
    main()