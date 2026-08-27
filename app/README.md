![Python](https://img.shields.io/badge/Python-3.13-blue)

![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)

![LanceDB](https://img.shields.io/badge/VectorDB-LanceDB-orange)

![Groq](https://img.shields.io/badge/LLM-Groq-red)

![License](https://img.shields.io/badge/License-MIT-yellow)

# 🚀 Cost-Efficient RAG Pipeline

A lightweight Retrieval-Augmented Generation (RAG) pipeline built using **FastAPI**, **LanceDB**, **Sentence Transformers**, and **Groq LLM**. The system ingests PDF documents, generates embeddings, stores them in a vector database, retrieves the most relevant chunks, and produces grounded responses with source citations.

---

## 📌 Features

- 📄 PDF document ingestion
- ✂️ Recursive text chunking
- 🧠 Local embedding generation using BAAI/bge-small-en-v1.5
- 🗄️ LanceDB vector database
- 🔍 Semantic similarity search
- 🤖 Groq LLM integration
- 📚 Source citation
- ⚡ FastAPI REST API
- 📈 Performance metrics
- ♻️ Idempotent ingestion (prevents duplicate chunks)

---

## 🏗️ Architecture

```
                PDF Documents
                      │
                      ▼
             Document Loader
                      │
                      ▼
             Document Chunker
                      │
                      ▼
            Embedding Model
        (BAAI/bge-small-en-v1.5)
                      │
                      ▼
                LanceDB
          (Vector Database)
                      │
             User Question
                      │
                      ▼
               Retriever
                      │
                      ▼
            Retrieved Chunks
                      │
                      ▼
              Prompt Builder
                      │
                      ▼
                Groq LLM
                      │
                      ▼
      Answer + Source Citations
```

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| API | FastAPI |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | LanceDB |
| LLM | Groq |
| Document Loader | LangChain |
| Chunking | RecursiveCharacterTextSplitter |
| Environment | python-dotenv |

---

# 📂 Project Structure

```
Cost-Efficient-RAG/
│
├── app/
│   ├── api.py
│   ├── chunker.py
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── llm.py
│   ├── loader.py
│   ├── rag.py
│   ├── retriever.py
│   ├── utils.py
│   ├── vector_store.py
│   └── __init__.py
│
├── data/
│   ├── raw/
│   └── lancedb/
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/cost-efficient-rag.git

cd cost-efficient-rag
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_api_key

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

VECTOR_DB_PATH=data/lancedb

TABLE_NAME=documents

CHUNK_SIZE=500

CHUNK_OVERLAP=50
```

---

# 📥 Ingest Documents

Place PDFs inside

```
data/raw/
```

Run

```bash
python -m app.ingest
```

---

# 🚀 Start API

```bash
python -m uvicorn app.api:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoint

## POST /ask

### Request

```json
{
    "question":"What are the course outcomes?",
    "k":3
}
```

### Response

```json
{
    "question":"What are the course outcomes?",
    "answer":"...",
    "sources":[
        "frmCourseSyllabusIPDownload.pdf (Page 0)"
    ],
    "retrieved_chunks":3,
    "retrieval_time":0.021,
    "generation_time":0.842,
    "total_time":0.871
}
```

---

# ⚡ Performance Metrics

The API returns:

- Retrieval Time
- Generation Time
- Total Pipeline Time
- Retrieved Chunks

These metrics help evaluate system efficiency.

---

# 📌 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Cross Encoder Re-ranking
- Multi-document Retrieval
- Streaming Responses
- Docker Deployment
- Authentication
- Evaluation Framework

---

# 👨‍💻 Author

**Abhay Shakya**

MCA (Artificial Intelligence & Machine Learning)

Python | Machine Learning | Generative AI | RAG | LangChain

LinkedIn: https://www.linkedin.com/in/abhayshakya/

GitHub: https://github.com/Musiccraz