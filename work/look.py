def claen(word):
    return word.strip().lower()

def lookUpWord(word):
    newword = ""
    for char in word:
        if char in 'aeiou':
            newword += char
    return newword
if __name__ == '__main__':
	try:
	    with open(r'dictionary.txt') as f:
	        for word in f:
	            word = claen(word)
	            wordstr = lookUpWord(word)
	            if wordstr == 'aeiou':
	                print(word)
	finally:
	    f.close()