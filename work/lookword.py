def claen(word):
    return word.strip().lower()

def lookupword(word):
    vowelsInWord = ""
    for char in word:
        if char in 'aeiou':
            vowelsInWord +=char
    return vowelsInWord

try:
    with open(r'dictionary.txt') as f:
        for word in f:
            word = claen(word)
            if len(word) < 5:
                continue
            vowelStr = lookupword(word)
            if vowelStr == 'aeiou':
                print(word)
finally:
    f.close()