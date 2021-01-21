import numpy as np
import pandas as pd
from xml.dom import minidom
import tensorflow as tf
import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import itertools
from nltk.stem import PorterStemmer

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def preprocessing(tokenize_text):
    pos_tag_text = pos_tag(tokenize_text)
    chunk_text = ne_chunk(pos_tag_text, binary=True)

    return chunk_text


def lemmatizer(word):
    lemma = nltk.wordnet.WordNetLemmatizer()
    return lemma.lemmatize(word)


def remove_stop_word(tokenize_text):
    stop_words = stopwords.words('english')
    stop_words.append('?')
    filtered_sentence = [w for w in tokenize_text if not w in stop_words]
    return filtered_sentence


def remove_already_used_word(tokenise_text_without_sw, words):
    filtered_text = []
    for w in tokenise_text_without_sw:
        if w.lower() not in words and w not in words:
            filtered_text.append(w)

    return filtered_text


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

def getCorpusConcat() :
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

    return c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10


# Return a bag of all stem words in all corpus
def getStemWords():
    words = getCorpusConcat()  
    words_tokenized = []

    words_tokenized = word_tokenize(words)
    # remove all tokens that are not alphabetic
    words_tokenized = [word for word in words_tokenized if word.isalpha()]

    lems = []

    for w in words_tokenized:
        lems.append(lemmatizer(w))  

    porter = PorterStemmer()

    words_stem = []

    for w in lems:
        words_stem.append(porter.stem(w))

    # Return without duplicates
    return list( dict.fromkeys(words_stem) )

# Return a bag of stem words for each corpus. Return 10 lists
def getStemWordsByCorpus():
    corpus = getCorpus()  
    wordsLists = []
 
    for c in corpus:
        wordsLists.append(word_tokenize(c))
    
    words_tokenized = []
    for words in wordsLists:
        # remove all tokens that are not alphabetic
        words_tokenized.append([word for word in words if word.isalpha()])

    lemsLists = []
    i = 0
    for words in words_tokenized:
        lemsLists.append([])
        for w in words: 
            lemsLists[i].append(lemmatizer(w))
        i+=1

    porter = PorterStemmer()
    j = 0
    words_stems = []
    for lems in lemsLists:
        words_stems.append([])
        for w in lems:
            words_stems[j].append(porter.stem(w))
        j+=1

    words_withoutDup = []
    for words in words_stems:
        words_withoutDup.append(list( dict.fromkeys(words) ))
    
    return words_withoutDup

if __name__ == "__main__":

    print(getStemWordsByCorpus()[0])

    # To remove duplicate, do : 
    # list = list( dict.fromkeys(mylist) )
