"""Geração de respostas utilizando LLM e conteúdo recuperado."""


def generate_answer(query: str, documents) -> str:
    """Combina ``query`` e ``documents`` para gerar a resposta final."""
    # TODO: integrar com modelo de linguagem
    print(f"Generating answer for '{query}' with {len(documents)} docs")
    return "Resposta gerada"
