import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim=384):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.bug_ids = []
    
    def add_embeddings(self, embeddings, bug_ids):
        embeddings_np = np.array(embeddings).astype('float32')
        self.index.add(embeddings_np)
        self.bug_ids.extend(bug_ids)
    
    def search(self, query_embedding, k=3):
        query_np = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_np, k)
        return distances[0], indices[0]
