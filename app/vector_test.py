from vector_store import LanceVectorStore

db = LanceVectorStore()

sample = [
    {
        "chunk_id": "1",
        "text": "Artificial Intelligence",
        "vector": [0.1] * 384,
        "source": "sample.pdf",
        "page": 1,
        "file_type": "pdf"
    }
]

db.create_table(sample)

print("Table created successfully.")