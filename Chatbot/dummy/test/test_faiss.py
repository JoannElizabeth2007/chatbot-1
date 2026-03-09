import faiss
import numpy as np

dim = 384
index = faiss.IndexFlatL2(dim)

vectors = np.random.rand(5, dim).astype("float32")
index.add(vectors)

query = np.random.rand(1, dim).astype("float32")
D, I = index.search(query, k=2)

print("FAISS search indices:", I)
