class BaseRetriever:
    """Base retriever interface."""

    def __init__(self, documents):
        self.documents = documents

    def retrieve(self, query, top_k=3):
        raise NotImplementedError


class TFIDFRetriever(BaseRetriever):
    """Simple TF-IDF retriever using scikit-learn."""

    def __init__(self, documents):
        super().__init__(documents)
        from sklearn.feature_extraction.text import TfidfVectorizer

        self.vectorizer = TfidfVectorizer()
        self.document_matrix = self.vectorizer.fit_transform(documents)

    def retrieve(self, query, top_k=3):
        query_vec = self.vectorizer.transform([query])
        scores = (self.document_matrix @ query_vec.T).toarray().ravel()
        ranked = scores.argsort()[::-1][:top_k]
        return [(self.documents[i], float(scores[i])) for i in ranked]


class BM25Retriever(BaseRetriever):
    """Naive BM25 retriever implemented without external deps."""

    def __init__(self, documents, k1=1.5, b=0.75):
        super().__init__(documents)
        from collections import Counter, defaultdict
        import math

        self.k1 = k1
        self.b = b
        self.tokenized = [doc.split() for doc in documents]
        self.n = len(documents)
        self.avgdl = sum(len(t) for t in self.tokenized) / float(self.n)
        self.doc_freqs = []
        df = defaultdict(int)
        for tokens in self.tokenized:
            freq = Counter(tokens)
            self.doc_freqs.append(freq)
            for token in freq:
                df[token] += 1
        self.idf = {w: math.log(1 + (self.n - f + 0.5) / (f + 0.5)) for w, f in df.items()}

    def _score(self, query_tokens, idx):
        import math

        score = 0.0
        freq = self.doc_freqs[idx]
        dl = len(self.tokenized[idx])
        for token in query_tokens:
            if token in freq:
                idf = self.idf.get(token, 0)
                tf = freq[token]
                denom = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                score += idf * (tf * (self.k1 + 1)) / denom
        return score

    def retrieve(self, query, top_k=3):
        tokens = query.split()
        scores = [self._score(tokens, idx) for idx in range(self.n)]
        ranked = sorted(range(self.n), key=lambda i: scores[i], reverse=True)[:top_k]
        return [(self.documents[i], float(scores[i])) for i in ranked]


def get_retriever(name, documents):
    """Factory for retrievers.

    Parameters
    ----------
    name : str
        Name of the retriever ("tfidf" or "bm25").
    documents : list[str]
        Collection of texts to index.
    """
    name = name.lower()
    if name == "tfidf":
        return TFIDFRetriever(documents)
    if name == "bm25":
        return BM25Retriever(documents)
    raise ValueError(f"Unknown retriever: {name}")


__all__ = [
    "BaseRetriever",
    "TFIDFRetriever",
    "BM25Retriever",
    "get_retriever",
]

