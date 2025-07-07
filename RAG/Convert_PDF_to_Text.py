from PyPDF2 import PdfReader
from langchain.schema import Document


def extract_text_with_pypdf(pdf_path):
    reader = PdfReader(pdf_path)
    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:  # Skip pages with no text
            documents.append(Document(page_content=text, metadata={"page": i + 1}))

    return documents

# Example usage
docs = extract_text_with_pypdf("C:/Users/jacin/Downloads/Jacinth London Appian.pdf")
for doc in docs:
    print(f"Page {doc.metadata['page']}:")
    print(doc.page_content)

print(docs)


