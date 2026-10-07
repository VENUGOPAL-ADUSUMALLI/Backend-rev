from reranker import rerank

query = "What is Django ORM?"

documents = [
    "Python is a high-level programming language widely used for backend development.",

    "Django includes an ORM that allows developers to interact with databases using Python objects.",

    "FastAPI supports asynchronous programming and is commonly used to build high-performance APIs."
]

results = rerank(query, documents)

for document, score in results:
    print(f"\nScore: {score}")
    print(document)