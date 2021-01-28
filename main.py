from collections import OrderedDict

import numpy as np
import pandas as pd
from xml.dom import minidom
import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import itertools
from nltk.stem import PorterStemmer


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


def getCorpus():
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

    return [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]


def getCorpusConcat():
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
    return list(dict.fromkeys(words_stem))


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
        i += 1

    porter = PorterStemmer()
    j = 0
    words_stems = []
    for lems in lemsLists:
        words_stems.append([])
        for w in lems:
            words_stems[j].append(porter.stem(w))
        j += 1

    words_withoutDup = []
    for words in words_stems:
        words_withoutDup.append(list(dict.fromkeys(words)))

    return words_withoutDup


def getIncidenceMatrix():
    dictionnary = getStemWords()
    corpusList = getStemWordsByCorpus()

    matrix = []
    i = 0
    for corpus in corpusList:
        matrix.append([])
        for word in dictionnary:
            if word in corpus:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
        i += 1
    return matrix


def getReversedIndex():
    dictionnary = getStemWords()
    corpusList = getStemWordsByCorpus()

    index = []
    i = 0

    for word in dictionnary:
        index.append([])
        index[i].append(word)
        j = 0
        for corpus in corpusList:
            if word in corpus:
                index[i].append(j)
            j += 1
        i += 1
    return index


def booleanRequest(request):
    print('------------')
    print('Request : ' + request)
    # Process
    words_token = word_tokenize(request)
    lems = []
    for w in words_token:
        lems.append(lemmatizer(w))
    porter = PorterStemmer()
    words = []
    for w in lems:
        words.append(porter.stem(w).lower())

    dictionnary = getStemWords()
    index = getReversedIndex()

    request = []
    # We replace the words by the corpus index it is in
    for i in range(len(words)):
        if words[i] != 'and' and words[i] != 'or' and words[i] != 'not' and words[i] != '(' and words[i] != ')':
            w = dictionnary.index(words[i])
            request.append(index[w][1:])

            if len(words) > i + 1:
                if words[i + 1] != 'and' and words[i + 1] != 'or' \
                        and words[i + 1] != 'not' and words[i + 1] != '(' and words[i + 1] != ')':
                    request.append('and')

        else:
            request.append(words[i])

    print('')
    print(words)
    print(request)

    result = treat_request(request)

    print(result)


def treat_request(request):
    i = 0
    # Remove the parenthesis
    while len(request) > 1 and i < len(request):
        if request[i] == '(':
            request.pop(i)
            tmp = treat_request(request[i:])
            del request[i:]

            for j in range(len(tmp)):
                request.insert(i + j, tmp[j])
            i = 0
        elif request[i] == ')':
            request.pop(i)
            tmp = treat_sub_request(request[0:i])
            del request[0:i]
            request.insert(0, tmp)
            return request
        else:
            i += 1

    # Treat the request left without parenthesis
    print(request)
    request = treat_sub_request(request)

    return list(OrderedDict.fromkeys(request))


def treat_sub_request(request):
    while len(request) > 1:
        for i in range(len(request)):
            if i == 2 and request[i] != 'not':
                tmp = basic_operation(
                    request[i - 2], request[i], request[i - 1])
                request.insert(i + 1, tmp)
                request.pop(i)
                request.pop(i - 1)
                request.pop(i - 2)
                break
            elif request[i] == 'not':
                tmp = basic_operation(request[i + 1], None, 'not')
                request.pop(i + 1)
                request.pop(i)
                request.insert(i, tmp)
                break

    return request[0]


def basic_operation(corpus_1, corpus_2, operator, corp_max=10):
    tmp = []
    if operator == 'and':
        for c in corpus_1:
            if c in corpus_2:
                tmp.append(c)
    elif operator == 'or':
        for c in corpus_1:
            tmp.append(c)
        for c in corpus_2:
            tmp.append(c)
    elif operator == 'not':
        tmp = [i for i in range(corp_max)]
        if corpus_1 is not None:
            for c in corpus_1:
                if c in tmp:
                    tmp.remove(c)

    return tmp


if __name__ == "__main__":
    
    booleanRequest("disease AND severe AND pneumonia")
    
    booleanRequest("antibody AND plasma AND (cells OR receptors)")
    
    booleanRequest("antimalarial drugs OR antiviral agents OR immunomodulators")
    
    booleanRequest("NOT plasma AND risk of infection AND restrictions")
    
    booleanRequest("(older adults AND antibodies) AND NOT (genomes OR variant)")
    
    booleanRequest("antibody treatments")
    
    booleanRequest("efficacy and safety of the treatments")
    
    booleanRequest("family access to hospitals")
    
    booleanRequest("contact tracing results")

    # print(getStemWords().index("develop"))
    # print(getReversedIndex()[300])
    # print(getReversedIndex()[301])
