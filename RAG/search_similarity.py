from langchain_community.vectorstores import FAISS
import pickle
from huggingface_hub import login
from langchain.retrievers import EnsembleRetriever

def search(query,embedding,k=5):

    new_vector_store = FAISS.load_local(

        "faiss_index",embedding,allow_dangerous_deserialization=True
    )
    docs=new_vector_store.similarity_search(query,k=k)
    return docs