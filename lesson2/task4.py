sentence = input('Input sentence: ')
words = sentence.split(' ')

for i, word in enumerate(words):
    if len(word) > 10:
        word = word[0:10] + '...'
    print(str(i + 1) + '.', word)
