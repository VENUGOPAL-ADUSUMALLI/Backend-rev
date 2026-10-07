from pathlib import Path

import chromadb
from rank_bm25 import BM25Okapi

from openai_embeddings import create_embedding
from reranker import rerank


TOP_K = 10
FINAL_K = 3


def tokenize(text):
    return text.lower().split()


def create_bm25(chunks):
    tokenized_chunks = [
        tokenize(chunk)
        for chunk in chunks
    ]

    return BM25Okapi(tokenized_chunks)


def keyword_search(query, chunks, bm25, top_k):
    query_tokens = tokenize(query)

    scores = bm25.get_scores(query_tokens)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [chunk for chunk, score in ranked[:top_k]]


def main():

    # -------------------------
    # 1. Load Chroma
    # -------------------------

    project_root = Path(__file__).resolve().parent.parent

    chroma_path = project_root / "chroma_db"

    client = chromadb.PersistentClient(
        path=str(chroma_path)
    )

    collection = client.get_collection(
        name="backend_documents"
    )


    # -------------------------
    # 2. Query
    # -------------------------

    query = "What is Django ORM?"

    query_embedding = create_embedding(query)


    # -------------------------
    # 3. Semantic Search
    # -------------------------

    semantic_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    semantic_chunks = semantic_results["documents"][0]

    print("\n========== SEMANTIC SEARCH ==========")

    for chunk in semantic_chunks:
        print("\n", chunk)


    # -------------------------
    # 4. BM25 Search
    # -------------------------

    # Get all chunks stored in Chroma
    all_data = collection.get()

    all_chunks = all_data["documents"]

    bm25 = create_bm25(all_chunks)

    keyword_chunks = keyword_search(
        query,
        all_chunks,
        bm25,
        TOP_K
    )

    print("\n========== KEYWORD SEARCH ==========")

    for chunk in keyword_chunks:
        print("\n", chunk)


    # -------------------------
    # 5. Combine results
    # -------------------------

    combined_chunks = list(
        dict.fromkeys(
            semantic_chunks + keyword_chunks
        )
    )

    print("\n========== COMBINED ==========")

    for chunk in combined_chunks:
        print("\n", chunk)


    # -------------------------
    # 6. Rerank
    # -------------------------

    ranked_chunks = rerank(
        query,
        combined_chunks
    )

    print("\n========== RERANKED ==========")

    for chunk, score in ranked_chunks:
        print(f"\nScore: {score}")
        print(chunk)


    # -------------------------
    # 7. Final context
    # -------------------------

    final_chunks = [
        chunk
        for chunk, score in ranked_chunks[:FINAL_K]
    ]

    context = "\n\n".join(final_chunks)

    print("\n========== FINAL CONTEXT ==========")
    print(context)


if __name__ == "__main__":
    main()