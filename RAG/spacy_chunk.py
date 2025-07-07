import spacy


def chunk_spacy():
# Load spaCy's English language model
    nlp = spacy.load("en_core_web_sm")

# Step 1: Read your text file
    with open('C:/Users/jacin/Desktop/optima_respore.txt', "r", encoding="utf-8") as file:
        text = file.read()

# Step 2: Process the text with spaCy
    doc = nlp(text)

# Step 3: Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents]

# Step 4: Chunk sentences (e.g., group every 3 sentences together)
    chunk_size = 3
    chunks = [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]

# Display the chunks
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}:", chunk)
        print('************************************************************')
    return chunks
chunk_spacy()