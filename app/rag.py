import faiss
import numpy as np
from app.config import client
from app.knowledge_loader import load_knowledge

VECTOR_PATH = "vector_store/knowledge.index"

knowledge = load_knowledge()
documents = list(knowledge.values())

index = faiss.read_index(VECTOR_PATH)

def retrieve(query, k=3):
    q_emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    _, idx = index.search(np.array([q_emb]).astype("float32"), k)

    return [documents[i] for i in idx[0]]
