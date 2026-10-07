from pathlib import Path

from rank_bm25 import BM25Okapi


def tokenize(text):
    return text.lower().split()


def create_bm25(chunks):
    tokenized_chunks = [
        tokenize(chunk)
        for chunk in chunks
    ]

    return BM25Okapi(tokenized_chunks)


def keyword_search(query, chunks, bm25, top_k=5):
    query_tokens = tokenize(query)

    scores = bm25.get_scores(query_tokens)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent

    file_path = project_root / "data" / "backend.txt"

    text = file_path.read_text(encoding="utf-8")

    chunks = text.split("\n\n")

    bm25 = create_bm25(chunks)

    query = "What is Django ORM?"

    results = keyword_search(
        query,
        chunks,
        bm25,
        top_k=3
    )

    for chunk, score in results:
        print(f"\nScore: {score}")
        print(chunk)