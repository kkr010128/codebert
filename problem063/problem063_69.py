import sys
abc='abcdefghijklmnopqrstuvwxyz'
sentences = sys.stdin.read()
for letter in abc:
    print( letter + ' : ' + str(sentences.lower().count(letter)))