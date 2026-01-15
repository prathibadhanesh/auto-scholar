import chromadb
from chromadb.utils import embedding_functions
import uuid

class VectorStore:
    def __init__(self, collection_name="health_research"):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        # Using default embedding function (sentence-transformers/all-MiniLM-L6-v2)
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_fn
        )

    def add_documents(self, documents, metadatas=None):
        ids = [str(uuid.uuid4()) for _ in documents]
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_text, n_results=5):
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results

if __name__ == "__main__":
    # Simple test
    vs = VectorStore()
    vs.add_documents(["Vitamin D is good for bones.", "Exercise reduces stress."])
    res = vs.query("What are the benefits of Vitamin D?")
    print(res)
