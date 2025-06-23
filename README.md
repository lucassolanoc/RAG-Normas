# RAG-Normas

Este repositório fornece uma estrutura inicial para a implementação de um sistema
Retrieval Augmented Generation (RAG) focado em normas técnicas. A organização
abaixo serve como base para ingestão de documentos, criação de índices e
interação via LLM.

```
RAG-Normas/
├── data/            # Arquivos de normas técnicas (PDFs, etc.)
├── docs/            # Documentação do projeto
├── src/             # Código-fonte do sistema
│   ├── ingestion/   # Scripts de ingestão e pré-processamento
│   ├── retrieval/   # Lógica de busca e indexação
│   └── generation/  # Integração com modelos de linguagem
├── tests/           # Casos de teste
└── README.md        # Descrição do projeto
```

## Hugging Face Inference API

O módulo `src/generation/generate.py` utiliza a Inference API da Hugging Face
para gerar respostas. Configure as seguintes variáveis de ambiente ao executar
`src/app.py`:

- `HF_MODEL`: identificador do modelo no Hub (padrão `google/flan-t5-base`)
- `HF_API_TOKEN`: token de autenticação (opcional para modelos públicos)
