# NanoRAG Assistant

NanoRAG Assistant is a lightweight, modular Retrieval-Augmented Generation (RAG) framework built for experimenting with knowledge-grounded AI systems using GPT-4 Nano.

It demonstrates how to combine document retrieval with large language models to produce accurate, context-aware answers.

This project focuses on clean architecture and real-world RAG system design, not just chatbot demos.

## Features

Modular RAG pipeline (Ingestion → Retrieval → Generation)

Vector-based semantic search using FAISS

Clean, production-style project structure

Plug-and-play OpenAI integration

Safe demo mode (runs without API key)

Easy to extend with PDFs, databases, or web data

## System Architecture
```bash
User Query
    ↓
Vector Similarity Search (FAISS)
    ↓
Relevant Knowledge Chunks
    ↓
GPT-4 Nano
    ↓
Final Grounded Answer
```

## Project Structure
```
nano-rag-assistant/
│
├── app/
│   ├── __init__.py
│   ├── config.py              # OpenAI & system configuration
│   ├── knowledge_loader.py    # Loads text knowledge base
│   ├── ingest.py              # Builds vector database
│   ├── rag.py                 # Semantic retrieval logic
│   └── main.py                # Gradio chat interface
│
├── knowledge-base/
│   └── employees/
│       └── lancaster.txt       # Sample knowledge file
│
├── vector_store/               # Stores FAISS index
├── requirements.txt
├── .env.example
└── README.md
```
## Installation
1. Clone repository
```
git clone https://github.com/ujjesha1312/nano-rag-assistant.git
cd nano-rag-assistant
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Configure environment (optional)

Create a .env file:
```
OPENAI_API_KEY=your_api_key_here
```
If no API key is provided, the system runs in demo mode.

### Build Vector Database
```
python -m app.ingest
```
### Expected output:

Loaded documents: 1
Vector store created successfully

Run the Assistant
```
python -m app.main
```

Open the browser UI and ask:
```
Who is Alex Lancaster?
Answer: Alex Lancaster is the CTO at NanoRAG Corp...
```
### Example Use Cases

Internal company knowledge assistant

University helpdesk chatbot

Product documentation Q&A system

Lightweight enterprise search engine
