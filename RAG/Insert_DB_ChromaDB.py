from langchain_community.vectorstores import Chroma
from langchain.embeddings.base import Embeddings
from langchain.schema import Document

def store_chunks_in_chromadb(embedding_model: Embeddings, chunks: list, collection_name: str = "rag_collection") -> Chroma:
    """
    Store text chunks into a Chroma vector database.

    Args:
        embedding_model (Embeddings): An initialized LangChain-compatible embedding model.
        chunks (list): A list of strings or Documents representing text chunks.
        collection_name (str): The name of the Chroma collection to use.

    Returns:
        Chroma: The Chroma vector store instance.
    """

    # If chunks are raw strings, convert them into Document objects
    documents = [Document(page_content=chunk) if isinstance(chunk, str) else chunk for chunk in chunks]

    # Create or load Chroma DB with the embedding model
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        collection_name=collection_name,
        persist_directory="./chroma_db"
    )
