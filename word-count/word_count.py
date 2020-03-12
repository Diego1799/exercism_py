from collections import Counter
from re import findall


def count_words(sentence):
    palabra = findall("[a-z0-9]+(?:'[a-z])?", sentence.lower())
    return Counter(palabra)
