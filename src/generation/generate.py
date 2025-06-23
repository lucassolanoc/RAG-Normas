"""Geração de respostas utilizando LLM e conteúdo recuperado."""

from typing import List


def generate_answer(query: str, documents: List[str]) -> str:
    """Combina ``query`` e ``documents`` para gerar uma resposta simples."""
    print(f"Generating answer for '{query}' with {len(documents)} docs")

    # Nesta implementação simplificada, apenas concatenamos trechos
    context = "\n".join(documents)
    snippet = context[:500]
    return f"Pergunta: {query}\n\nTrechos:\n{snippet}"
