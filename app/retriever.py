from app.embeddings import EmbeddingModel
from app.vector_store import LanceVectorStore

class Retriever:

    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.vector_store = LanceVectorStore()
        self.table = self.vector_store.get_table()

    def retrieve(self, query, k=3):
        query_vector = self.embedding_model.embed_query(query)

        results = (
            self.table
            .search(query_vector)
            .limit(k)
            .to_list()
        )


        return results