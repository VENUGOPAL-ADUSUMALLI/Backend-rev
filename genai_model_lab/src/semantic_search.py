from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def main() -> None:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    documents = [
        "Python is used for backend development",
        "Django is a Python web framework",
        "Java is popular for enterprise applications",
        "Cricket is a popular sport in India",
        "FastAPI is useful for building APIs",
    ]

    query = "i want to play cricket"

    document_embeddings = model.encode(documents)
    query_embedding = model.encode([query])

    similarity_scores = cosine_similarity(
        query_embedding,
        document_embeddings,
    )[0]

    ranked_results = sorted(
        zip(documents, similarity_scores),
        key=lambda item: item[1],
        reverse=True,
    )

    top_k = 3

    top_results = sorted(
        zip(documents, similarity_scores),
        key=lambda item: item[1],
        reverse=True,
    )[:top_k]

    print(f"Top {top_k} results:")
    print("=" * 60)

    for document, score in top_results:
        print(f"Score: {score:.4f} | {document}")


if __name__ == "__main__":
    main()