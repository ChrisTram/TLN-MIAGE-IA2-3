import numpy as np
import pandas as pd
from xml.dom import minidom
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def getCorpus() : 
    with open('./corpus/c1.txt', encoding="utf8") as file:
        c1 = file.read().replace('\n', '')
    with open('./corpus/c2.txt', encoding="utf8") as file:
        c2 = file.read().replace('\n', '')
    with open('./corpus/c3.txt', encoding="utf8") as file:
        c3 = file.read().replace('\n', '')
    with open('./corpus/c4.txt', encoding="utf8") as file:
        c4 = file.read().replace('\n', '')
    with open('./corpus/c5.txt', encoding="utf8") as file:
        c5 = file.read().replace('\n', '')
    with open('./corpus/c6.txt', encoding="utf8") as file:
        c6 = file.read().replace('\n', '')
    with open('./corpus/c7.txt', encoding="utf8") as file:
        c7 = file.read().replace('\n', '')
    with open('./corpus/c8.txt', encoding="utf8") as file:
        c8 = file.read().replace('\n', '')
    with open('./corpus/c9.txt', encoding="utf8") as file:
        c9 = file.read().replace('\n', '')
    with open('./corpus/c10.txt', encoding="utf8") as file:
        c10 = file.read().replace('\n', '')

    return [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

if __name__ == "__main__":


    corpus = getCorpus()

    # Sentences to bag of words
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(corpus)


    #vocab_size = len(tokenizer.word_index) + 1

    encoded_docs = tokenizer.texts_to_sequences(corpus)
    print(encoded_docs)

    text_padded_sequence = pad_sequences(encoded_docs, maxlen=100)
    print(text_padded_sequence)
