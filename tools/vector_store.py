import chromadb
from tools.embedder import create_embedding

client = chromadb.PersistentClient(
    path="vector_db/chroma_db"
)

collection = client.get_or_create_collection(
    name="study_material"
)



def store_chunks(chunks):

    for i, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk],
        )

def search(query):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results["documents"][0]