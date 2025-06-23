"""Mecanismos de busca para as normas técnicas."""

from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:
    """Busca documentos relevantes utilizando TF-IDF."""

    def __init__(self, documents: List[str]):
        # ``stop_words`` aceita apenas ``None`` ou ``'english'`` por padrão.
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(documents)
        self.documents = documents

    def search(self, query: str, top_k: int = 3) -> List[str]:
        """Retorna ``top_k`` documentos mais relevantes para ``query``."""
        print(f"Searching for '{query}'")
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.doc_vectors).flatten()
        ranked = scores.argsort()[::-1]
        return [self.documents[i] for i in ranked[:top_k]]
