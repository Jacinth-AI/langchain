from  langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from uuid import uuid4
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
import pickle
import faiss

def insert_docs(embedding,documents):
    dimension=384
    Index=faiss.IndexFlatL2(dimension)
    vector_store=FAISS(
        embedding_function=embedding,
        index=Index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={}
    )

    uuids=[str(uuid4()) for _ in range(len(documents))]
    vector_store.add_documents(documents=documents,ids=uuids)
    vector_store.save_local("faiss_index")
    