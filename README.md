# RAG-Normas

Exemplo simples de uso de *retrievers* em um fluxo RAG. 

Este repositório inclui uma implementação básica de dois mecanismos de
recuperação de documentos: **TF‑IDF** e **BM25**. A escolha do tipo de retriever
é feita através de um único parâmetro.

## Como utilizar

1. Instale as dependências (somente `scikit-learn` é necessária):

```bash
pip install scikit-learn
```

2. Execute o exemplo passando o tipo de retriever desejado (`tfidf` ou
   `bm25`):

```bash
python example.py bm25
```

Isso irá imprimir na tela os documentos recuperados e a pontuação
atribuída por cada algoritmo.
