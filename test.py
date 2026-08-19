from app.embeddings.embedder import Embedder

embedder = Embedder()
vector = embedder.embed("AWS IAM manages users.")

print(vector.shape)