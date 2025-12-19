import re
import nltk
import spacy
from collections import Counter

nltk.download('stopwords')
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
STOPWORDS = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    doc = nlp(text)

    tokens = [
        token.lemma_
        for token in doc
        if token.text not in STOPWORDS and len(token.text) > 2
    ]
    return tokens

if __name__ == "__main__":
    raw_text = """
    I absolutely loved the product! The delivery was fast,
    but the packaging was terrible and disappointing.
    """

    tokens = clean_text(raw_text)
    print("Cleaned Tokens:", tokens)

    word_freq = Counter(tokens)
    print("\nTop Words:")
    for word, freq in word_freq.most_common(5):
        print(word, freq)