"""Example usage for the retrievers module."""

from retrievers import get_retriever

docs = [
    "o rato roeu a roupa do rei de roma",
    "a raposa marrom pula sobre o cachorro preguiçoso",
    "um pequeno passo para o homem, um grande salto para a humanidade",
]


def run_example(kind: str = "tfidf"):  # pragma: no cover
    retriever = get_retriever(kind, docs)
    res = retriever.retrieve("passo homem", top_k=2)
    for doc, score in res:
        print(f"{score:.4f}: {doc}")


if __name__ == "__main__":  # pragma: no cover
    import sys

    kind = sys.argv[1] if len(sys.argv) > 1 else "tfidf"
    run_example(kind)

