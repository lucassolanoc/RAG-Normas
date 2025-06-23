import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ingestion.ingest import ingest_documents


def test_ingest_documents():
    docs = ingest_documents('data')
    assert isinstance(docs, list)
    assert len(docs) > 0
