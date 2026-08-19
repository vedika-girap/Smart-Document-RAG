import numpy as np

from app.embeddings.embedder import Embedder
from app.models.document import Document
from app.vector_store.faiss_store import FaissStore


def test_faiss_search():
    embedder = Embedder()

    documents = [
        Document(
            content="AWS IAM manages users and permissions.",
            metadata={"filename": "aws.txt"},
        ),
        Document(
            content="Amazon S3 stores objects.",
            metadata={"filename": "aws.txt"},
        ),
        Document(
            content="Amazon EC2 provides virtual servers.",
            metadata={"filename": "aws.txt"},
        ),
    ]
    texts = [doc.content for doc in documents]

    vectors = embedder.embed_documents(texts)

    vectors = np.array(vectors, dtype= "float32")

    store = FaissStore(dimension=vectors.shape[1])
    store.add(vectors, documents)

    query = embedder.embed("How does AWS IAM manage permissions?")
    query = np.array([query], dtype="float32")

    results = store.search(query, k=2,)
    assert len(results) == 2

    document, score = results[0]

    print(document.content)
    print(score)

    assert "IAM" in document.content


# def test_faiss_store():
#     embedder = Embedder()

#     texts =[
#         "AWS IAM manages users and permissions.",
#         "Amazon S3 stores objects.",
#         "Amazon EC2 provides virtual servers.",
#     ]

#     vectors = embedder.embed_documents(texts)

#     store = FaissStore(dimension=384)
#     store.add(np.array(vectors,dtype="float32"))

#     query = embedder.embed(
#         "How does IAM manage permissions?"
#     )

#     scores, indices = store.search(
#         np.array([query], dtype="float32"), k = 2)

#     print(scores)
#     print(indices)
#     print(indices.shape)
#     assert indices.shape == (1, 2)

