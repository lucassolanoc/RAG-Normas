"""Módulos para ingestão de normas técnicas."""

from pathlib import Path


def ingest_documents(data_path: str) -> None:
    """Processa documentos em ``data_path`` e prepara para indexação."""
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Pasta inexistente: {data_path}")
    # TODO: implementar leitura de arquivos e criação de embeddings
    print(f"Ingesting documents from {path.resolve()}")
