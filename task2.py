import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

#reversing the string
reverseList = randomPhrase[::-1]
randomPhrase

#print the string
print(randomPhrase)
print(reverseList)

