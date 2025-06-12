"""Exemplo simples de uso do sistema RAG para normas técnicas."""

from ingestion.ingest import ingest_documents
from retrieval.retriever import search
from generation.generate import generate_answer


def main() -> None:
    data_path = "data/normas"
    ingest_documents(data_path)

    query = input("Consulta: ")
    docs = search(query)
    answer = generate_answer(query, docs)
    print(answer)


if __name__ == "__main__":
    main()
