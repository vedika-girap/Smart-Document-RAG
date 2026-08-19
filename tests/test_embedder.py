from app.embeddings.embedder import Embedder

def test_embedder():
    embedder = Embedder()
    vector = embedder.embed("AWS IAM manages users")
    assert vector.shape == (384,)
