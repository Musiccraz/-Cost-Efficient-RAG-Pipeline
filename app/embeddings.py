from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL

class EmbeddingModel:

    def __init__(self):
        print(f"Loading embedding model: {EMBEDDING_MODEL}")
        self.model = SentenceTransformer(EMBEDDING_MODEL)

        print("Embedding dimension:", self.model.get_embedding_dimension())

    def embed_documents(self,texts):
        return self.model.encode(
            texts,
            convert_to_numpy =True,
            show_progress_bar =True

        )

    def embed_query(self,query):
        return self.model.encode(
            query,
            convert_to_numpy=True
        )
