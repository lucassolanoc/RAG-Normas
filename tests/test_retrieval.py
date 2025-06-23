import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from ingestion.ingest import ingest_documents
from retrieval.retriever import Retriever


def test_retrieval_search():
    docs = ingest_documents('data')
    r = Retriever(docs)
    results = r.search('tensao')
    assert isinstance(results, list)
    assert len(results) > 0
