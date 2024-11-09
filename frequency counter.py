
import re
from collections import Counter

def word_frequency(text):
    """
    Count the frequency of each word in a given text.

    Args:
        text (str): Input text.

    Returns:
        dict: Word frequencies.
    """
    
    text = re.sub(r'[^\w\s]', '', text).lower()
    
    
    words = text.split()
    
    
    word_freq = Counter(words)
    
    return word_freq

def main():
    
    text = input("Enter a paragraph: ")
    
    
    word_freq = word_frequency(text)
    
    
    print("Word Frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()
