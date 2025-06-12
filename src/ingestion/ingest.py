"""Módulos para ingestão de normas técnicas."""

from pathlib import Path

from retrieval import retriever


def ingest_documents(data_path: str) -> None:
    """Processa documentos em ``data_path`` e prepara para indexação."""
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Pasta inexistente: {data_path}")

    documents = []
    for file in path.rglob("*.txt"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        documents.append({"path": str(file), "content": text})

    retriever.add_documents(documents)
    print(f"Ingesting {len(documents)} documents from {path.resolve()}")
