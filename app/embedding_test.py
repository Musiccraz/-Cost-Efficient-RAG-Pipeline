from pathlib import Path

from loader import DocumentLoader
from chunker import DocumentChunker
from embeddings import EmbeddingModel

BASE_DIR = Path(__file__).resolve().parent.parent

loader = DocumentLoader(BASE_DIR / "data" / "raw")
documents = loader.load_documents()

chunker = DocumentChunker()
chunks = chunker.split_documents(documents)

embedding_model = EmbeddingModel()

texts = [chunk.page_content for chunk in chunks]

vectors = embedding_model.embed_documents(texts)

print("Number of chunks:", len(chunks))
print("Number of vectors:", len(vectors))
print("Vector dimension:", len(vectors[0]))