"""Mecanismos de busca para as normas técnicas."""

from typing import List, Dict


DOCUMENTS: List[Dict[str, str]] = []


def add_documents(docs: List[Dict[str, str]]) -> None:
    """Adiciona documentos ao índice em memória."""
    DOCUMENTS.extend(docs)


def search(query: str):
    """Realiza busca no índice e retorna documentos relevantes."""
    print(f"Searching for '{query}'")
    query_lower = query.lower()
    results = []
    for doc in DOCUMENTS:
        if query_lower in doc["content"].lower():
            results.append(doc)

    return results
