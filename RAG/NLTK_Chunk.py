import nltk
from nltk.tokenize import sent_tokenize


def chunk_NLTK():
# Make sure to download the necessary NLTK resources
    print('end1')  
    nltk.download('punkt_tab')
    # Open and read a text file
    with open('C:/Users/jacin/Desktop/optima_respore.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    print(text)

# Step 2: Tokenize it into sentences
    sentences = sent_tokenize(text)

# Step 3: Chunk into groups (e.g., every 3 sentences as one chunk)
    chunk_size = 3
    chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]

# Now your chunks are ready for embedding and storing in your vector DB
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:", chunk)
       

    
    return chunks

chunk_NLTK() 
