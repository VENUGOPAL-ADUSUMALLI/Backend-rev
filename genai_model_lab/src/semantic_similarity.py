from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def main() -> None:
    model = SentenceTransformer("all-MiniLM-L6-v2")

    sentences = [
        "I love Python",
        "Python is my favorite programming language",
        "I want to play cricket",
    ]

    embeddings = model.encode(sentences)

    similarity_matrix = cosine_similarity(embeddings)

    for i, sentence_a in enumerate(sentences):
        for j, sentence_b in enumerate(sentences):
            if i < j:
                score = similarity_matrix[i][j]

                print("=" * 60)
                print("Sentence A:", sentence_a)
                print("Sentence B:", sentence_b)
                print(f"Similarity score: {score:.4f}")


if __name__ == "__main__":
    main()