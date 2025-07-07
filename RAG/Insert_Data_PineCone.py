import os
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pinecone import ServerlessSpec, PodSpec 

def store_chunks_in_pinecone(embeddings, api_key, docs):
    os.environ['PINECONE_API_KEY'] = api_key
    
    pc = Pinecone(api_key=api_key)
    index_name = "developer-quickstart-py"

    if index_name in pc.list_indexes():
        pc.delete_index(index_name)

    spec = PodSpec(
    environment="us-east-1-aws",
    pod_type="p1.x1"
    )
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=spec  
    )  

    vectorstore_from_docs = PineconeVectorStore.from_documents(
        docs,
        index_name=index_name,
        embedding=embeddings
    )
    return vectorstore_from_docs
