
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parent
DOCUMENT_PATH = BASE_DIR / "sample.txt"
CHROMA_PATH = BASE_DIR / "chroma_db"

LLM_MODEL = "llama3.2:3b"
EMBEDDING_MODEL = "nomic-embed-text"


def build_vectorstore():
    loader = TextLoader(
        str(DOCUMENT_PATH),
        encoding="utf-8",
    )
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s)")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
    )
    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL,
    )
    vectorstore = Chroma(
        collection_name="local_rag",
        embedding_function=embeddings,
        persist_directory=str(CHROMA_PATH),
    )
    collection = vectorstore._collection
    if collection.count() == 0:
        vectorstore.add_documents(chunks)
        print("Documents indexed successfully.")
    else:
        print("Using existing ChromaDB collection.")

    return vectorstore

def main():
    vectorstore = build_vectorstore()
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3},
    )
    llm = ChatOllama(
        model=LLM_MODEL,
        temperature=0,
    )

    print("\nLocal RAG is ready!")
    print("Type 'exit' to stop.\n")

    while True:
        question = input("Ask a question: ").strip()

        if not question:
            continue

        if question.lower() == "exit":
            break

        try:
            retrieved_docs = retriever.invoke(question)
            print("\n--- Retrieved Context ---")
            if not retrieved_docs:
                print("No relevant documents found.")
                continue
            for index, doc in enumerate(retrieved_docs, start=1):
                print(f"\nChunk {index}:")
                print(doc.page_content)
            context = "\n\n".join(
                doc.page_content for doc in retrieved_docs
            )
            prompt = f"""
You are a helpful technical tutor.

Answer the user's question using the supplied context.

Rules:
- Explain the answer clearly in 2-4 sentences when appropriate.
- Answer directly instead of repeating the topic.
- Do not invent facts that are not supported by the context.
- If the context does not contain the answer, say:
  "I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

            response = llm.invoke(prompt)
            print("\n--- Answer ---")
            print(response.content)
            print()
        except Exception as error:
            print(f"\nError processing question: {error}\n")


if __name__ == "__main__":
    main()
