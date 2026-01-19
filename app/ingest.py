import faiss
import numpy as np
from app.config import client
from app.knowledge_loader import load_knowledge

VECTOR_PATH = "vector_store/knowledge.index"

def build_index():
    knowledge = load_knowledge()
    docs = list(knowledge.values())

    print("Loaded documents:", len(docs))

    embeddings = []
    for doc in docs:
        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=doc
        )
        embeddings.append(emb.data[0].embedding)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))

    faiss.write_index(index, VECTOR_PATH)
    print("Vector store created successfully")

if __name__ == "__main__":
    build_index()
