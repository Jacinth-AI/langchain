from langchain.text_splitter import RecursiveCharacterTextSplitter

# Example: use your existing list of Document objects (e.g., from PdfReader or PDFLoader)
# Let's say your variable is called `docs`
def CONVERT_TEXT_to_CHUNCKS(size,overlap,docs):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=size,      # Number of characters per chunk
        chunk_overlap=overlap     # Overlap to preserve context across chunks
        )

    chunks = text_splitter.split_documents(docs)
    return chunks
    
