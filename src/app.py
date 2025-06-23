"""Exemplo simples de uso do sistema RAG para normas técnicas."""

from ingestion.ingest import ingest_documents
from retrieval.retriever import Retriever
from generation.generate import generate_answer


def main() -> None:
    data_path = "data"
    documents = ingest_documents(data_path)
    retriever = Retriever(documents)

    query = input("Consulta: ")
    docs = retriever.search(query)
    answer = generate_answer(query, docs)
    print(answer)


if __name__ == "__main__":
    main()
