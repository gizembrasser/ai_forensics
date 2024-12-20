import re
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def get_synonyms(keywords):
    expanded_keywords = set(keywords)

    # Get expanded keywords list including synonyms
    for keyword in keywords:
        for synset in wordnet.synsets(keyword):
            for lemma in synset.lemmas():
                expanded_keywords.add(lemma.name().replace('_', ' '))
    return list(expanded_keywords)

def contains_keywords(answer, keywords):
    if not answer or not keywords:
        return False  # Return False if the answer or keywords list is empty

    expanded_keywords = get_synonyms(keywords)

    # Create a regex pattern to match any of the expanded keywords, case-insensitive
    pattern = re.compile('|'.join(re.escape(keyword) for keyword in expanded_keywords), re.IGNORECASE)

    # Search for keywords in the answer
    return bool(pattern.search(answer))
