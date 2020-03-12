def find_anagrams(word, candidates):
    candidate = []
    word = word.lower()
    for words in candidates:
        x = words.lower()
        if word != x and sorted(word) == sorted(x):
            candidate.append(words)
    return candidate
