import re

txt = 'The rain in Spain'
x = re.search(r"\bS\w+", txt)
print(x.group())

def checkWord(regex):
    resList = []
    with open('wordlist.txt') as wordFile:
        for line in wordFile:
            if re.match(regex, line[:-1]): # or line.strip()
                resList.append(line[:-1]) # line.strip()
        return resList

def rail_break(cipherText):
#    word_dict = create_word_dict("word-list.txt")
    cipher_len = len(cipherText)
    max_good_so_far = 0
    best_guess = 'No words found in dictionary'
    for i in range(2, cipher_len + 1):
        words = rail_decrypt(cipherText, i)
        good_count = 0
        for w in words:
            good_count += 1
            if good_count >= max_good_so_far:
                max_good_so_far = good_count
                best_guess = ' '.join(words)
        return best_guess
    
def rail_decrypt(cipher_text, num_rails):
    rail_len = len(cipher_text) // num_rails
    solution = ''
    for col in range(rail_len):
        for rail in range(num_rails):
            next_letter = col + (rail * rail_len)
            solution += cipher_text(next_letter)
        return solution.split()

def letterFrequency(text):
    text = text.lower()
    nonLetters = removeMatches(text, 'abcdefghijklmnopqrstuvwxyz')
    text - removeMatches(text, nonLetters)
    lCount = {}
    total = len(text)
    for ch in text:
        lCount[ch] = lCount.get(ch, 0) + 1

    for ch in lCount:
        lCount[ch] = lCount[ch] / total
    return lCount

def removeMatches():
    pass

def maybeAdd(ch, toList):
    if ch in 'abcdefghijklmnopqrstuvwxyz' and ch not in toList:
        toList.append(ch)

