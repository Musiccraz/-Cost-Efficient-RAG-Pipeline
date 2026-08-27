from pathlib import Path
from loader import DocumentLoader
from chunker import DocumentChunker

BASE_DIR = Path(__file__).resolve().parent.parent

loader = DocumentLoader(BASE_DIR / "data" / "raw")
documents = loader.load_documents()

print("Documents:", len(documents))

chunker = DocumentChunker()
chunks = chunker.split_documents(documents)

print("Chunks:", len(chunks))

if chunks:
    print("=" * 50)
    print(chunks[0].page_content[:300])
    print(chunks[0].metadata)
else:
    print("No chunks created.")