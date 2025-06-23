"""Geração de respostas utilizando LLM e conteúdo recuperado."""

from __future__ import annotations

import os
from typing import List

import requests


HF_MODEL = os.getenv("HF_MODEL", "google/flan-t5-base")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# Configurações para servidor Ollama local
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-r1:8b")
USE_OLLAMA = os.getenv("USE_OLLAMA", "0") == "1"


def _hf_inference(prompt: str) -> str:
    """Realiza chamada à Inference API da Hugging Face."""
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"} if HF_API_TOKEN else {}
    response = requests.post(url, headers=headers, json={"inputs": prompt}, timeout=30)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list) and data and "generated_text" in data[0]:
        return data[0]["generated_text"]
    if isinstance(data, dict) and "generated_text" in data:
        return data["generated_text"]
    return str(data)


def _ollama_inference(prompt: str) -> str:
    """Realiza chamada a um servidor Ollama local."""
    url = f"{OLLAMA_URL.rstrip('/')}/api/generate"
    body = {"model": OLLAMA_MODEL, "prompt": prompt, "stream": False}
    response = requests.post(url, json=body, timeout=60)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, dict) and "response" in data:
        return data["response"]
    return str(data)


def generate_answer(query: str, documents: List[str]) -> str:
    """Combina ``query`` e ``documents`` para gerar uma resposta utilizando a Inference API."""
    print(f"Generating answer for '{query}' with {len(documents)} docs")

    context = "\n".join(documents)
    snippet = context[:1000]
    prompt = f"Pergunta: {query}\n\nContexto:\n{snippet}"

    try:
        if USE_OLLAMA:
            return _ollama_inference(prompt)
        return _hf_inference(prompt)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Inference failed: {exc}")
        return prompt
