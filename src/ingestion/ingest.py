"""Módulos para ingestão de normas técnicas."""

from pathlib import Path
from typing import List

from pypdf import PdfReader


def ingest_documents(data_path: str) -> List[str]:
    """Processa documentos em ``data_path`` e retorna textos extraídos."""
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Pasta inexistente: {data_path}")

    documents: List[str] = []
    for pdf_file in path.glob("*.pdf"):
        reader = PdfReader(str(pdf_file))
        text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )
        documents.append(text)

    if not documents:
        raise ValueError(f"Nenhum PDF encontrado em {data_path}")

    print(f"Ingested {len(documents)} document(s) from {path.resolve()}")
    return documents
