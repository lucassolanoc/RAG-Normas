"""Geração de respostas utilizando LLM e conteúdo recuperado."""


def generate_answer(query: str, documents) -> str:
    """Combina ``query`` e ``documents`` para gerar a resposta final."""
    print(f"Generating answer for '{query}' with {len(documents)} docs")

    if not documents:
        return "Nenhum documento encontrado para responder à consulta."

    snippet = "\n\n".join(doc["content"][:200] for doc in documents[:3])
    resposta = f"Pergunta: {query}\n\nTrechos relevantes:\n{snippet}"
    return resposta
