from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love Python",
    "Python is my favorite programming language",
]

embeddings = model.encode(sentences)

for sentence, embedding in zip(sentences, embeddings):
    print("=" * 60)
    print("Sentence:", sentence)
    print("Vector:", embedding)
    print("Vector dimension:", len(embedding))