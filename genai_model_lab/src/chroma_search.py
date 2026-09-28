import chromadb
from  sentence_transformers import  SentenceTransformer

from src.real_embeddings import embedding


def main():
    model = SentenceTransformer("all-MiniLM-L6-v2")

    documents = [
        "Python is used for backend development",
        "Django is a Python web framework",
        "Java is popular for enterprise applications",
        "Cricket is a popular sport in India",
        "FastAPI is useful for building APIs",
    ]
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="backend_documents")
    embeddings = model.encode(documents).tolist()
    collection.add(
        ids=[f"doc_{index}" for index in range(len(documents))],
        documents=documents,
        embeddings=embeddings,
    )

    query = "I want to learn python backend development"
    query_embeddings = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embeddings,
        n_results=3
    )
    print("query: ", query)
    print("=" * 60)
    for document, distance in zip(
            results["documents"][0],
            results["distances"][0],
    ):
        print(f"Distance: {distance:.4f} | {document}")

if __name__ == "__main__":
    main()

