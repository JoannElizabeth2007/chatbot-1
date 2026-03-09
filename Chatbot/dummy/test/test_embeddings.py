import time
from sentence_transformers import SentenceTransformer

start = time.time()
model = SentenceTransformer("all-MiniLM-L6-v2")
elapsed = time.time() - start

print("Load time:", round(elapsed, 2), "seconds")
print("Vector shape:", model.encode("test").shape)
