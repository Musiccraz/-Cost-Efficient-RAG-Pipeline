from pathlib import Path

from app.loader import DocumentLoader
from app.chunker import DocumentChunker
from app.embeddings import EmbeddingModel
from app.vector_store import LanceVectorStore

from app.utils import generate_chunk_id

BASE_DIR = Path(__file__).resolve().parent.parent


def main():

    print("=" * 60)
    print("Loading Documents")
    print("=" * 60)

    loader = DocumentLoader(BASE_DIR / "data" / "raw")
    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")

    print("=" * 60)
    print("Chunking")
    print("=" * 60)

    chunker = DocumentChunker()
    chunks = chunker.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("=" * 60)
    print("Generating Embeddings")
    print("=" * 60)

    embedding_model = EmbeddingModel()

    texts = [chunk.page_content for chunk in chunks]

    vectors = embedding_model.embed_documents(texts)

    print(f"Generated {len(vectors)} vectors")

    print("=" * 60)
    print("Preparing Records")
    print("=" * 60)

    records = []

    for chunk, vector in zip(chunks, vectors):

        records.append({

            "chunk_id": generate_chunk_id(chunk),

            "text": chunk.page_content,

            "vector": vector.tolist(),

            "source": chunk.metadata.get("source"),

            "page": chunk.metadata.get("page"),

            "file_type": chunk.metadata.get("file_type")

        })

    print(f"Prepared {len(records)} records")

    print("=" * 60)
    print("Saving to LanceDB")
    print("=" * 60)

    db = LanceVectorStore()

    db.get_table()

    existing_ids = db.get_existing_chunk_ids()

    new_records = []

    for record in records:
        if record["chunk_id"] not in existing_ids:
            new_records.append(record)


    print(f"Existing Records : {len(existing_ids)}")
    print(f"New Records : {len(new_records)}")

    if new_records:
        db.add_data(new_records)


    print("Finished!")


if __name__ == "__main__":
    main()